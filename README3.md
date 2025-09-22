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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8abcb9e5-74b9-3b6f-8c05-50c19c1dec26 | -12.70343 | -40.47471 | 2025-09-22 00:11:00 | TERRA_M-M | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 37c18f86-93d1-3b24-a8a1-339359c50068 | -10.36653 | -46.11827 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5ed97cf4-b0b4-3c30-b6cd-42506d85b6aa | -14.2681 | -44.38345 | 2025-09-22 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2616a60b-a638-34a2-95c5-f90134026393 | -10.39299 | -46.09172 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 164795ef-b967-3c87-a4c2-6de15d3602db | -11.77024 | -44.89939 | 2025-09-22 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 750a4ba3-dd96-3ef1-af9c-f6e94b77c3cf | -7.18624 | -42.24934 | 2025-09-22 00:11:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3bfb643b-f40a-3748-879f-627581ca7240 | -14.69277 | -48.79519 | 2025-09-22 00:11:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 555a6c01-9d20-3a9f-ad9f-77ef15fef860 | -10.50579 | -44.04913 | 2025-09-22 00:11:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b8f4011b-5860-3947-adca-1f3944f0371d | -14.97838 | -44.41296 | 2025-09-22 00:11:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 10cbb375-6e3d-3087-b4a6-61ff7beaa45b | -14.23108 | -44.31651 | 2025-09-22 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2e8d3aa3-2da5-3324-bdac-d6c0e7129b25 | -10.32159 | -46.09665 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3fa03248-45fd-345e-b430-f0d04dbe65c0 | -7.5068 | -43.68739 | 2025-09-22 00:11:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 70c61c2b-e11a-34fe-b943-94d789f73e84 | -11.76891 | -44.88925 | 2025-09-22 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1906b426-ecfa-3445-b8e3-aa486104fae4 | -10.43084 | -46.1379 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 25366d12-7424-325f-a1ff-f8df22d9bb33 | -10.41707 | -46.12276 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 281e9aa3-5d84-3b76-8b0c-42eb9d485f06 | -10.40575 | -46.11279 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| df4d358d-e92b-36de-98f7-e8033f877b8c | -10.46196 | -44.19573 | 2025-09-22 00:11:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3a425d28-7091-3618-831e-83bb46b0240d | -14.63392 | -48.2635 | 2025-09-22 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 88a088e9-7cce-3470-a793-fef86193ff6e | -10.68557 | -46.45538 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b9c01053-1471-3fde-be3d-4a70a18391da | -7.93232 | -44.09838 | 2025-09-22 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c7d703f6-5ec5-3bd5-9f37-165aaf4c1990 | -11.26474 | -49.24321 | 2025-09-22 00:11:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 62003dac-6e59-398a-b57f-8dc325be1cb0 | -8.67626 | -41.50453 | 2025-09-22 00:11:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 6e06da21-420f-33a1-a0cd-8174d057320a | -11.26527 | -49.23653 | 2025-09-22 00:11:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1bfb1204-4319-347c-a3fa-77f91c6a330f | -10.69269 | -46.43102 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| d7780455-2f39-3f9a-b553-da16539de837 | -8.52597 | -44.9321 | 2025-09-22 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ed72dd6-b50b-3871-a2d8-5cca8863a907 | -9.47821 | -40.37144 | 2025-09-22 00:11:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 33f5fddd-7173-33e7-863a-46462a432451 | -15.09938 | -43.84978 | 2025-09-22 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f70c7acc-3ab9-3824-b140-502742d705b3 | -12.98172 | -46.38781 | 2025-09-22 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 7ac5806c-072b-31d4-b33c-980c0eaa1254 | -7.46258 | -42.63461 | 2025-09-22 00:11:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 26743280-df4b-389c-9b60-9cbfd3dab787 | -7.17716 | -42.25062 | 2025-09-22 00:11:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| af4686ad-db97-3eb4-b0ad-e56814eb0641 | -7.82105 | -46.48735 | 2025-09-22 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eef2a4c5-b4af-3fe1-804c-e3dc43614c04 | -14.11891 | -44.01505 | 2025-09-22 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 577b7cdf-33dd-396e-9085-d130be0d09c4 | -8.52472 | -44.92279 | 2025-09-22 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 54a22bb3-33ee-36d1-b162-b3b7cc7064ce | -11.21753 | -49.60257 | 2025-09-22 00:11:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1594aa6c-c344-3ca3-9d5a-8ae2523fb213 | -14.69121 | -48.78016 | 2025-09-22 00:11:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ac1068c2-d667-3daa-9f7f-22ce07b6b393 | -7.80089 | -46.18583 | 2025-09-22 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 9735255b-520a-3146-be83-03c73073feaf | -11.66469 | -47.49767 | 2025-09-22 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| df50e5fa-d5a2-38e6-a338-f45cdb24cfa4 | -9.9945 | -46.23846 | 2025-09-22 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6f8b945b-4f5c-346d-af63-724481582066 | -7.61088 | -44.44099 | 2025-09-22 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d5e15b21-0d6a-397a-adbf-8a0a25f7c872 | -11.80834 | -41.16541 | 2025-09-22 00:11:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 27.5 |
| ea168b53-0365-3b69-a020-387f610b2847 | -11.64091 | -44.33781 | 2025-09-22 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6c78439f-0ca7-33f2-b55f-2fb92e35074e | -13.54937 | -43.32696 | 2025-09-22 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 24ae7e73-46ed-357f-bc71-b22fa551c4f3 | -13.08173 | -47.01523 | 2025-09-22 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 967f3a43-2731-346d-9aeb-ceb04d321def | -10.32308 | -46.10782 | 2025-09-22 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cc560800-21ce-37b4-9ee2-aeb7e58b4278 | -11.26755 | -49.25631 | 2025-09-22 00:11:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aeb37ce9-e31c-3d8d-b6ff-a7cd7d85a5ed | -9.19471 | -44.63474 | 2025-09-22 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5c56dddc-a4d6-35cb-8bad-10bf0ae48a78 | -8.86099 | -46.15265 | 2025-09-22 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 283ff02b-0461-3dad-8eb4-22482574aead | -4.87024 | -45.82299 | 2025-09-22 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c60bee76-10e3-326d-ba12-3f8326d97842 | -6.89346 | -44.78302 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30f2dee8-129f-32fa-879a-38285dc54c6b | -6.4451 | -45.68472 | 2025-09-22 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1439b805-4118-3907-8999-0efd503a34d9 | -7.36172 | -44.5616 | 2025-09-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 82e7a2dd-725b-397b-9880-19508cd67ce3 | -5.59132 | -46.25112 | 2025-09-22 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e313fa75-fa09-3185-97bb-75cb98376124 | -5.75751 | -43.62365 | 2025-09-22 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2eead9d8-a568-3e48-b89d-a808f840e179 | -5.25476 | -43.06893 | 2025-09-22 00:13:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0cf3ad92-58d7-3529-967a-f8a6caaf0649 | -7.35076 | -44.56027 | 2025-09-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 40ffb902-23c6-3d40-8af8-2a0187e6a9d1 | -3.86628 | -43.09678 | 2025-09-22 00:13:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2caea504-7d4c-3149-81ae-a831c3bfd1f4 | -5.76757 | -43.63125 | 2025-09-22 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 11ee0c62-4e64-3d57-9e3f-03a629bd44e5 | -5.76633 | -43.62241 | 2025-09-22 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e27f97cc-79f4-36bc-80a1-45e8650a9c4a | -6.53377 | -43.31928 | 2025-09-22 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4190e261-2e22-3fe8-ae26-f08c670e7df8 | -4.44925 | -46.90762 | 2025-09-22 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 0737ff9c-2039-32d6-8f99-51eb0625e169 | -7.23261 | -45.1753 | 2025-09-22 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2b615611-45e4-3f98-b5dd-ed4d939c2136 | -7.41801 | -46.39793 | 2025-09-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1f8e98bb-42c3-3642-b08e-f5648f0dcb01 | -6.90111 | -44.77268 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| dddf035c-a37f-3665-b2e3-8e941788a0dd | -7.43209 | -46.40044 | 2025-09-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 94f8e74a-7817-30cb-bea5-4074ea6216cb | -5.41748 | -45.51149 | 2025-09-22 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0185de0c-58ba-3d92-86de-7c0d1284d058 | -5.64385 | -45.95849 | 2025-09-22 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 2e2acfac-29f3-3282-88e8-a2737f814c73 | -7.02728 | -46.30391 | 2025-09-22 00:13:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31de8d2c-78bd-3b8d-94c1-19b6b4e6496f | -5.83188 | -49.03044 | 2025-09-22 00:13:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a0017575-dffa-3902-8894-65707a65da1d | -7.23048 | -43.75434 | 2025-09-22 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1725b47-d6d3-3006-860b-ef9ce1ef14dc | -4.99026 | -45.14985 | 2025-09-22 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e576c0ca-89cf-32ce-8bf1-e7dd843db486 | -4.43332 | -43.06379 | 2025-09-22 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5e0194a-fc65-3d51-a8f8-68b7ce7a2399 | -6.9729 | -44.75699 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e351d21e-dba9-386d-9b28-7c51a65004fe | -5.66662 | -44.44484 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdf6b253-5468-33ad-9f8c-f5e1a3cab436 | -4.52299 | -44.02811 | 2025-09-22 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09ff76c2-3b31-3b91-b56e-fc5ad88838bf | -5.66784 | -44.45366 | 2025-09-22 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ea171551-9e73-31a1-8414-cb3cd0f3d049 | -7.2317 | -43.76316 | 2025-09-22 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1da40065-93b2-319c-8f44-32f2d3fb7d83 | -7.42247 | -46.40175 | 2025-09-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 282.0 |
| e835a2f2-0837-3137-807e-854c9b2efc57 | -6.45426 | -45.68349 | 2025-09-22 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9e37d9ca-7a3f-3655-af2a-edfff139a0d8 | -5.64254 | -45.94884 | 2025-09-22 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a44700aa-686e-3c2e-add0-19a462896a79 | -2.25288 | -47.88932 | 2025-09-22 00:13:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b0dda7d7-a7f6-3524-ba26-9ec05ef74a8c | -4.25022 | -48.60419 | 2025-09-22 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 755997e7-1209-3056-b86c-3cca2f78678d | -5.0676 | -40.47178 | 2025-09-22 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 66f07177-ca2c-3cc7-9aa1-76a187ddbe0b | -5.74013 | -44.16212 | 2025-09-22 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a81a92d-3e13-3f3f-8ebc-b40e465cf187 | -4.70862 | -42.08597 | 2025-09-22 00:13:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 61584462-43ef-3fc7-bc61-4c89e208c89a | -6.44639 | -45.69429 | 2025-09-22 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 481620e8-28a2-371d-a0a2-38e5811cf132 | -1.34517 | -47.74695 | 2025-09-22 00:13:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6a72536b-2212-3b99-8cd6-cb5696756c04 | -6.19811 | -45.3573 | 2025-09-22 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48560b75-0534-3461-a8ec-8a34d21d4648 | -5.41874 | -45.52072 | 2025-09-22 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54da7ff2-9810-33f1-ab6c-84acda7482fc | -7.0287 | -46.3144 | 2025-09-22 00:13:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5103c6f6-e4df-3872-8d0c-f51783a1d090 | -3.05118 | -46.93049 | 2025-09-22 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8bb0d5c9-cbb5-32f8-b0a5-30ac60fc21cd | -5.75875 | -43.6325 | 2025-09-22 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 87108ce5-9728-3d4c-a689-df164c7afd7b | -5.59264 | -46.26093 | 2025-09-22 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0f931ab7-8893-35d2-816f-55a1401d3451 | -5.57473 | -48.98988 | 2025-09-22 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 46a377ef-7a61-3c12-88ca-704fa60b1123 | -2.25133 | -47.87817 | 2025-09-22 00:13:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1efa1dd0-9908-30c6-8d88-352e760ea443 | -6.56612 | -43.47171 | 2025-09-22 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f851c2a9-d6e6-3ba4-bcc5-94bc0f7a773c | -4.86896 | -45.81355 | 2025-09-22 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1906544-2585-3750-82bc-054c685699e8 | -5.33208 | -44.82293 | 2025-09-22 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e48bbd81-67f6-3080-9503-22038665529f | -4.71799 | -42.08461 | 2025-09-22 00:13:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 054938a2-1e7c-3608-99d9-dfb78764c0c6 | -4.87803 | -45.81225 | 2025-09-22 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1d56b2d7-f218-3252-9d6e-beadf8a34d06 | -5.33524 | -44.17792 | 2025-09-22 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |


[Clique aqui para ver as próximas entradas](README4.md)
