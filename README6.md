# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03b47c50-5dcf-36b5-9ec3-ceb88f1d1f9a | -20.47786 | -53.67476 | 2025-03-02 05:05:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7272fc9c-9b82-3aae-8ba7-c2d2ded1edbe | -20.91542 | -56.54497 | 2025-03-02 05:05:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30dcc9c0-315d-3a27-aec0-aa3a8f7d580d | -17.67002 | -54.16276 | 2025-03-02 05:05:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e43c9e0-ca63-3f0b-9e3d-4ade3c7ac8e7 | -20.91892 | -56.54554 | 2025-03-02 05:05:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2119a01-72f3-373d-ac88-eb577ac08b8a | -17.67384 | -54.16325 | 2025-03-02 05:05:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ece4fc25-42a3-363c-bde5-c5f52ec292c9 | 1.3217 | -60.4262 | 2025-03-02 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 99b1b82d-28d6-38f7-ba8e-caab1d59fa57 | 1.19789 | -60.06714 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b487fc7-0108-3898-8a3f-09ea42883ad1 | 2.1905 | -61.85543 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9623a96f-f043-3eb9-8335-6cb4016beb35 | 1.19643 | -60.06918 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef482b3c-57a7-3c72-ab8b-64d5aec83916 | 0.92236 | -59.39989 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caa760b9-8a44-396e-941c-84ccb472ec76 | 2.00308 | -60.55871 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6c698f2-f896-35fa-9fa0-20b9556034fe | 3.76464 | -59.99133 | 2025-03-02 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9e3dad5-3aa6-3659-b9b4-77d6b1882407 | 1.68935 | -60.22886 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 749ec174-408b-30e1-b7a7-b31a6be9b8ff | 0.13346 | -60.39939 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 783c33a0-5654-397a-b2a9-6e10ad3956f2 | 1.99383 | -60.55606 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5b25691-36a9-3730-b616-e1eba6e30edf | 0.13414 | -60.40384 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8635c19a-f120-38e9-8f5a-d7fdafd9db54 | 0.81113 | -59.77092 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c8a9c30-572d-3c14-94da-fadded488052 | 0.80934 | -59.64145 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88fe7f7e-c256-3a27-9c3e-1f5eb9736b90 | 3.23754 | -60.46904 | 2025-03-02 05:52:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3a0b0d7-8bcf-38c8-8ffd-90e02ebdda87 | 2.58133 | -60.62586 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c4e6e4f7-bf78-3714-ad00-aa4d694489ed | 3.10518 | -60.45635 | 2025-03-02 05:52:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c945589-6f8c-3b03-b33e-039b18039a8e | 1.65366 | -60.28667 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f51d9e75-a04c-34f2-84d3-3a469065a8f5 | 1.01069 | -60.3866 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9124539-5f94-3115-95b8-1f352edd2dd7 | 1.32277 | -60.42192 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82342f20-c6f6-31fc-84fe-77fd6f5d9922 | 2.41134 | -60.00081 | 2025-03-02 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829398c4-ca94-3faf-ba26-8f60c67fdf74 | 2.40761 | -60.00594 | 2025-03-02 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5603ec73-8f60-3b0e-b0bf-b4d0f8da29ba | 2.57735 | -60.62486 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1f7845b0-09d0-3da9-9fbf-f1de3bb8eb00 | 0.77412 | -60.54785 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74fbcb11-eb13-3a4e-a89a-925cb2775718 | 2.1114 | -61.81622 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 01d601f3-47b4-3ec4-8b8c-514dfbbc7eb2 | 1.9365 | -60.39095 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a371b120-dbc0-39f9-877f-0c351db805db | 0.96556 | -60.53059 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76a14820-0b75-348d-9e39-b19f425fc981 | 1.42505 | -60.80189 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ad70b65-236e-3010-9b46-18926274ba30 | 2.72113 | -61.04036 | 2025-03-02 05:52:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0f7d31c6-1f58-34dd-9836-2a17aa1d2897 | 2.58068 | -60.62188 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f045961-b951-30e7-985d-9ea05861755b | 2.1913 | -61.86048 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f538130-3b7e-31b4-bc55-4ded74a1b28f | 1.03214 | -59.56197 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b55387f-aaf3-377e-b2ff-f03f550d4002 | 4.25746 | -59.93423 | 2025-03-02 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a8bb71a-2571-3bb1-bef0-3cb4e32085d1 | 1.19587 | -60.30233 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c44b9987-aa05-3487-8a07-4e858afa33d2 | 1.94091 | -60.39054 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99318f79-08b4-3866-8a4a-b4f3dc097d2c | 2.18577 | -61.85101 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3debe7c6-a51b-3815-8d0c-cdfb3d918aaf | 1.9372 | -60.39531 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 278d79b2-4712-3270-a3e4-1cb89ecb95d6 | 2.58222 | -60.62815 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d009e47-baaf-35a5-8c67-5294d04e280a | 1.58997 | -59.96576 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67a45871-541c-3b26-be18-63bbaafc7dd4 | 1.20197 | -60.51347 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a5d015-c85c-3bdc-9ccd-d466da010f3c | 0.96926 | -60.52561 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bef8ac35-89c6-3a66-935b-72f9bc676272 | 1.65284 | -60.28342 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00e9b362-723c-3959-b56e-99d3d6df4cdb | 1.79047 | -60.66884 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a30cb63-1fc8-3970-a470-18e99c079273 | 1.32849 | -60.42975 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 350aa173-d3d4-329a-8664-f81443820fb5 | 0.64174 | -60.0079 | 2025-03-02 05:52:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d37801c-79a7-332d-b223-33ff2068f085 | 1.07273 | -59.54521 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bbf716a-f11b-33b4-8db5-8ba2020c7f5c | 0.76973 | -60.54856 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a499e9f9-9cda-3480-888f-de706a6c96d3 | 1.31533 | -60.4319 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 053b0b42-e223-3fbe-a1d3-c795d3869ad3 | 2.67096 | -61.40804 | 2025-03-02 05:52:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab769446-666c-3bd8-9cb3-3ce68562ab58 | 0.83022 | -59.94946 | 2025-03-02 05:52:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d59b2c0c-c913-3974-aee0-109f8af02463 | 3.54499 | -60.46307 | 2025-03-02 05:52:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ed7f2fab-043e-3b91-b176-3b94b125fbda | 0.96488 | -60.52634 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d461a41-a5f5-3ab0-88c1-4e80a811a953 | 1.31905 | -60.42691 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09ae13dd-57f0-3f25-9605-cc19fdd5621c | 1.1976 | -60.51418 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae6162cb-274b-3d48-ac42-a6309095ab38 | 2.22232 | -61.34303 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 211593e7-fc24-3f10-b4bc-57c242827e46 | 3.23394 | -60.47372 | 2025-03-02 05:52:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33459b12-cbe5-3d03-910d-354c14c77c17 | 0.85763 | -60.44866 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 550af0e4-4978-348e-934e-df519082cdde | 2.18657 | -61.85609 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c17b9471-e51c-3916-a697-87abd4086deb | 0.9568 | -60.53202 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9cba23d-40c1-386f-b6a2-d3d28536c641 | 0.64262 | -60.00999 | 2025-03-02 05:52:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b150c8f-5df9-3b5f-877d-a4a306370697 | 2.37215 | -60.45822 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 435348fe-11ae-30ab-986a-42c7f389a33d | 1.78982 | -60.66471 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96a36cfa-55a3-344f-bcc5-4631db83436d | 2.11535 | -61.81561 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab5c89c1-4738-3e5a-af0b-249de2beb0ef | 0.69869 | -60.27301 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e8ee0d7-d00e-3897-a34c-c093799c1df1 | 0.67658 | -59.6388 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 966d5898-a2f9-3afe-bb4d-3e86cac87549 | 1.3241 | -60.43046 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8f40de9a-c9af-3d8a-95fb-d01e31199489 | 1.03293 | -59.56692 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a062e780-ef30-3d94-a316-29b0a9d3595d | 0.67921 | -59.63962 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56f6c0d2-8406-340a-8b87-2a2e7849fe87 | 1.32783 | -60.42548 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea0ce2e7-7cb9-30d7-a6dc-1b6de7f5f21c | 0.67451 | -59.64033 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73838875-db58-31f6-aaa1-157e59a597fa | 1.31971 | -60.43118 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8a9f679b-2656-3045-bc35-21bab6d86945 | 1.3151 | -60.06402 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2dcde45-e93f-390d-a153-974736b7d9ca | 1.32343 | -60.42619 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6c9f4dc-20dc-30c7-96aa-92163720b9ed | 0.9605 | -60.52706 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 586ba17c-638a-3739-8aa0-401ddf5650f4 | 2.11647 | -61.81696 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c829a67d-0de9-3a2a-8ed6-cfc6eb88d821 | 1.65299 | -60.28234 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41884c40-23c5-384f-8f7a-01973c923d0c | 1.31132 | -60.06925 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cb7adbae-f9af-300b-a0ee-28304906cc42 | 0.96118 | -60.53131 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 545df376-96bd-38b5-9c2a-69b1e14c882f | 2.58159 | -60.62417 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd45a8ab-6330-3e2c-ba0e-401a2ae6a464 | 1.10546 | -59.58419 | 2025-03-02 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6e3c630-73d0-3d48-a0b4-56cbfe800a53 | 1.94019 | -60.38604 | 2025-03-02 05:52:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e209d2e6-d63d-3ad9-8510-f9801fc354cb | 2.11251 | -61.81757 | 2025-03-02 05:52:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0e9db66e-6c97-306a-8aee-50e1a7ac9a3b | 1.32038 | -60.43545 | 2025-03-02 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d625842a-d6a3-3d06-8192-f2e27aa030b5 | 0.96994 | -60.52987 | 2025-03-02 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c19815ee-a9e8-3636-a8f8-9b72619e1281 | 1.93473 | -60.38557 | 2025-03-02 06:18:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 633fa192-9828-3345-b7d7-4470667a09fc | 1.32339 | -60.42229 | 2025-03-02 06:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 03398518-1f7b-3f2a-b04e-6e468b4dc66a | 1.94145 | -60.37894 | 2025-03-02 06:18:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5dfb1c1b-5515-3d9c-8c37-f7e76f1d5964 | 1.9432 | -60.39108 | 2025-03-02 06:18:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1d994f28-c79f-3f67-9449-7faa4f0cf08b | 2.11299 | -61.80988 | 2025-03-02 06:18:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| eaff7c19-683b-3016-a1aa-80171e6fba9e | 2.58322 | -60.62053 | 2025-03-02 06:18:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ec62f18c-328a-3fd4-bc96-c1dea72d4f4f | 0.96974 | -60.52398 | 2025-03-02 06:18:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6a27fa2f-095b-31ef-960a-071b491fcdfc | 1.31253 | -60.06676 | 2025-03-02 06:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| db1b2f73-5b7d-3d03-a9b0-dfe6872820ca | 1.31302 | -60.42376 | 2025-03-02 06:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b40fd0f6-69c2-31b2-8647-c28fb221aa3c | 1.32521 | -60.43472 | 2025-03-02 06:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4528db99-0276-3c3d-9216-0b10daac7571 | 0.96754 | -60.52496 | 2025-03-02 06:18:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f321dd7f-b766-30aa-b360-4ec6093d953f | 1.31705 | -60.42656 | 2025-03-02 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README7.md)
