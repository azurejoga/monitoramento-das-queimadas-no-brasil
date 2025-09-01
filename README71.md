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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ffb40cd-1f9f-3bff-99b1-7f251a05c0b4 | -12.57526 | -44.80932 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f02c1105-cbbf-34e7-a891-78b5b50ba42e | -12.57233 | -48.20467 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c145cc13-ee1e-39c6-ad03-fe74c1ad6a12 | -12.96243 | -48.1096 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eab3ad15-ce62-33c7-a083-78ee3e74288b | -11.05584 | -52.04338 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53b9f261-570b-3aee-838a-2f454391fa18 | -13.69401 | -46.92208 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4122a66a-a0f2-315d-bf2e-18d782390284 | -12.96525 | -48.1137 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0353112-829a-3977-af9a-7c281a862e0f | -11.84941 | -46.78967 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a0d5884-a437-3e7f-95c7-302348ec36ca | -15.69221 | -52.75063 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07b47db5-d86d-32ef-af27-029c65daabef | -12.84337 | -48.07696 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5bc5d9d-8baa-3c92-9add-92a01d791f20 | -14.75676 | -46.76184 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b089c604-2c77-373a-b2e4-b78ecf637fbf | -13.54163 | -46.9741 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf276fa5-284e-3a01-9236-774c06c5a2d3 | -15.79733 | -48.21259 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a5b4898-9e78-327a-a49e-52c38d74ce2c | -11.02595 | -47.02864 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 355bd658-2209-3a1f-925d-ee8d69e3b085 | -13.66657 | -46.93557 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18365a77-a206-3ac1-9320-8cb2a8545e84 | -11.03053 | -47.02159 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 386276d8-0cff-345c-a069-c79fe5ec8d7f | -12.98074 | -54.75738 | 2025-09-01 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06331788-b788-3566-804d-331d2ef462de | -10.24155 | -51.12162 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e651d75e-bae4-3880-9d9e-849fec8a8fab | -15.58484 | -48.32404 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 622b9413-a5ea-3d6d-a1c4-9f59fcbf7c85 | -12.8674 | -48.06563 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e67e2c5e-2a42-384e-b59a-4f0c07b5bf11 | -14.04345 | -44.58419 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66bcfd5d-2633-3802-a690-f1ccbb89dbf7 | -16.29165 | -52.93781 | 2025-09-01 04:34:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43ffd3e1-fb54-3df4-a2ea-98e7a160ca32 | -11.37166 | -43.60004 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1229a8c-5867-3616-a0b4-09da331af59d | -15.59046 | -48.193 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 50d360cf-ff10-34c3-8e8a-adf1e9805d57 | -12.86935 | -48.16605 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef39a9d3-913f-3e16-8ad5-eedd1b952ad5 | -15.69612 | -48.91014 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d90ba92e-bc1e-333d-a480-14b603ecdcc3 | -11.89807 | -46.68866 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2e6b3f6-ebc4-3c5b-9add-00d310caf5eb | -16.0812 | -43.62283 | 2025-09-01 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17915135-9d29-3e75-bcf2-892734bb53b6 | -16.96779 | -49.31237 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65d826ee-1d9f-3fe0-983d-2f81ad34e4f3 | -11.02995 | -47.02538 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 83a41d22-51b7-3852-955e-15a0f079a739 | -13.3661 | -46.94427 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c86c37b4-e058-3f72-911f-7fd0d384152d | -12.09175 | -44.71848 | 2025-09-01 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ac77037-a03e-3090-9784-63d62ac792a6 | -13.38019 | -47.06773 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a1a2f90-1843-398f-aab9-740c07bd2277 | -11.04708 | -46.95875 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32e56cf5-7135-3084-8d46-490d2cc37871 | -14.74614 | -46.73399 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e46b8301-6218-3477-bef7-4cfb00c90fb3 | -12.87701 | -48.09307 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1429d77e-b80e-3bde-a916-7b94d9182b06 | -11.02596 | -46.98232 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c572c23a-966a-3c6d-b507-9da5b53d46da | -15.58884 | -48.34377 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 65958fae-ffe6-3eb0-969f-7428681ef788 | -16.9689 | -49.3051 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d4b7030-4486-33b0-9d34-025a317bcd61 | -12.83328 | -48.07537 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f347a28d-25f3-3977-8767-b496b094f86d | -11.07748 | -52.06834 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496735af-b191-3fed-ad3c-e9e941918ed9 | -11.79155 | -46.43044 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac93e3da-e1d7-3da9-aa37-f655ef08ed88 | -18.23389 | -48.1354 | 2025-09-01 04:34:00 | NOAA-20 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc4df140-e5ab-30b5-a957-6aac63551fdd | -11.05168 | -46.92848 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b46fa0eb-24d1-3d47-8f9c-6893dc6f7d41 | -14.6056 | -54.48694 | 2025-09-01 04:34:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d01172ab-68f4-3aad-8d70-73562c0e2527 | -15.72849 | -48.99018 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 64162506-c636-301a-b12e-f09d125e06c3 | -12.66483 | -48.21913 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6db5e442-40ff-36ef-9a83-f2aed0e8caa9 | -10.36848 | -52.29224 | 2025-09-01 04:34:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c9d032a-af92-3a17-aa23-19596b9677fa | -12.9658 | -48.11009 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db83fd79-befe-3270-af61-c74784921d94 | -13.31672 | -46.8599 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0dd3c8c-29c0-3987-ad75-5c2c93767452 | -10.93705 | -48.24684 | 2025-09-01 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1dd775f-b1cf-38d1-99f5-bd16af49024b | -12.32635 | -45.72015 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb26326f-be1e-3e50-b86a-54306a5ea7ec | -11.33069 | -43.68523 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd61d5b8-9081-3b7d-9f7a-cb1686cc3234 | -11.87604 | -46.7413 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bea032ff-7a90-3961-bf89-006d01d842c3 | -11.92981 | -50.6297 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c0a0a56-da94-3153-84ae-2d39b0d5167f | -14.8489 | -47.09457 | 2025-09-01 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a140e435-fa62-39fd-8f8d-69781df37512 | -11.07819 | -52.06411 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a1abe60-f573-36cc-8acf-341cc1c2680e | -12.58293 | -48.20267 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ca2f44b-0da0-3a07-a6a8-023653ce60b9 | -13.65099 | -48.15682 | 2025-09-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa1f5914-f1d2-3dc3-b934-5afabadc0f11 | -12.56007 | -48.21749 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd23b916-3f0e-35b9-b883-fe20a66f1bc1 | -12.84058 | -48.0727 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fad8c8ca-bf21-3e01-af2f-b77642c4b720 | -11.31188 | -55.13929 | 2025-09-01 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 214a169b-fdb6-3cb0-be86-f97d47969cbe | -15.69945 | -48.88816 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73457fa1-5acc-337e-b64e-5cf8fad47a4a | -14.7881 | -46.73463 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71c9429d-020e-3c15-9790-4bb3f22d1833 | -11.02366 | -46.95107 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec848225-2e9a-39a7-a5ba-2e460045ccc2 | -13.68704 | -46.92047 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d040157d-a8f5-3db3-81fe-0d5be4ca7e3b | -13.32078 | -46.85673 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66ea31cf-1929-3bd9-87fe-a973aeb871e6 | -16.08188 | -43.62052 | 2025-09-01 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13235782-bb20-3aee-b594-12a7dadadac1 | -10.87486 | -55.76255 | 2025-09-01 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 80253df8-e51f-3872-8b7a-02d4567f5c6a | -13.50715 | -46.98909 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e36e77a7-b4d7-32ca-bfa5-a32c48e52439 | -11.01263 | -46.83712 | 2025-09-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd4ae424-1e35-3de7-a07f-9e1265c7bd9d | -10.47621 | -51.63017 | 2025-09-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8d53f5f-ae03-369f-bb47-47311ffe5260 | -11.05112 | -46.90897 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 278a1afb-5df9-3679-8c09-84487388dbb1 | -15.9098 | -50.28792 | 2025-09-01 04:34:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75492fc2-42e7-36de-b3c9-98061f889fc3 | -16.4099 | -45.65555 | 2025-09-01 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f761d67-8718-3473-8bf2-8cb1b5ba7926 | -8.72993 | -62.39573 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 759f3c63-3404-33c0-b267-061d3631569f | -15.31522 | -46.07749 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6294f4f5-60dc-37a3-8082-2e68719665fc | -14.41962 | -51.66252 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71285a83-3526-36fd-b543-0989b312ed0e | -9.44208 | -60.57927 | 2025-09-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49b47e7e-57ff-3d26-943c-14d944e0328c | -11.89922 | -46.68089 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c88458c1-5748-387e-b7d2-540f30652075 | -13.47301 | -42.48131 | 2025-09-01 04:34:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fde0c9d5-dcdd-3bbc-ad72-a3516771c963 | -13.16575 | -45.28079 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa86a232-4ae4-3c48-a207-e645b3545e49 | -11.37063 | -43.60757 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27252815-306b-3220-964c-f21b04883689 | -8.72856 | -62.40261 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90941083-fd28-333f-a2b9-06d90a752443 | -13.31895 | -46.84478 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e41b8754-43c4-3446-9c2d-fcb67c3d2bdd | -10.89225 | -50.8364 | 2025-09-01 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 66ffc20a-6aa0-35e4-9411-fc734706af9d | -15.6152 | -47.85838 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f64fdcf-859a-3a63-be59-d479a1bcf975 | -11.04668 | -50.85707 | 2025-09-01 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c7d32bc-23eb-36ed-8d5c-d417ced4ee85 | -15.72402 | -48.99696 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| df4cbd88-f0f8-3a48-98f1-e1a18f4d0c4e | -11.37218 | -43.59625 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26032a61-29ce-3966-8b08-9631d7b48306 | -11.01795 | -46.96567 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b67c3e5e-4d6c-3810-9b50-faeef80d0483 | -12.60246 | -48.20951 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e3b4d93-1692-352a-9fba-69221e0482e9 | -13.18164 | -45.27831 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96fef685-9971-339f-bf49-383ce9201b9a | -13.66716 | -46.93157 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71742ace-7875-3ab4-bdff-d17439de36ee | -11.9636 | -51.36194 | 2025-09-01 04:34:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 112d28d8-999e-3bc1-a516-b4c678e04539 | -11.04765 | -46.97813 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7e67a20-f44f-3b7b-9e19-4b70904947bc | -14.75019 | -46.7566 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7071a890-e3d1-3c47-808a-da7817f72474 | -11.79088 | -46.45898 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e8dc43b-156f-3589-a1ba-35c97e2c8b2b | -13.69051 | -46.87148 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 914d14e9-0099-39f4-ae68-2505ad391131 | -11.01392 | -46.94577 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c5d446-3ae8-3821-9eac-b2443fa6c3d4 | -15.09746 | -48.14429 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README72.md)
