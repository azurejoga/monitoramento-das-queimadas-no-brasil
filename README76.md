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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a29c467-68ce-3b18-9201-ba65f0f5f578 | -5.7355 | -43.2916 | 2026-09-30 18:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ee41b28f-6e3e-390f-bab8-499f44d946ec | -15.9476 | -39.9576 | 2026-09-30 18:30:00 | GOES-19 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 315.2 |
| d5b612cf-b6ed-3a9d-9aa8-fc66f59eac02 | -11.6789 | -43.4921 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| cf98da88-be54-3bf9-a9c3-28b535d805e7 | -11.699 | -43.4416 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 233.4 |
| 7129253e-42f0-3e22-9bab-16ace0e415fc | -13.8685 | -43.9975 | 2026-09-30 18:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 219.7 |
| c7a584ce-35b2-3fd9-ab7c-149ffb543abb | 1.8586 | -55.6241 | 2026-09-30 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 25a8a645-038b-3778-9ab6-ffb9ca5a676d | -13.8784 | -44.4442 | 2026-09-30 18:30:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 0269faad-aa84-3d49-8424-616673944467 | -5.414 | -45.8958 | 2026-09-30 18:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 71d688ce-87df-355b-9c63-6ca1cd0b1ba4 | 1.822 | -55.6247 | 2026-09-30 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 7141ae18-05b2-394e-b910-19bbd323fa36 | -11.7182 | -43.4386 | 2026-09-30 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| ebfeec6e-db3e-3866-b5e0-aae7c858f74c | -9.8064 | -44.8265 | 2026-09-30 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 48375f98-71b1-3aba-8318-b89fbf72015f | -13.8784 | -44.4442 | 2026-09-30 18:40:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| d838023f-a062-3756-ab8d-00a66f441c2e | 4.1703 | -60.5734 | 2026-09-30 18:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 4dea77d5-ca38-378a-a301-2ec7b5e8b0e2 | -15.2234 | -46.157 | 2026-09-30 18:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 6025574d-6553-3a38-bd32-5ccd52af9f67 | -10.5197 | -45.3784 | 2026-09-30 18:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 2b956dc2-b6cb-330b-b5a9-30d15a240f05 | -15.9476 | -39.9576 | 2026-09-30 18:40:00 | GOES-19 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 115.0 |
| 832ec7c7-de82-3459-b7bd-fc559f873a58 | 3.53 | -60.6247 | 2026-09-30 18:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 91.6 |
| ce753173-3303-38a2-ac60-ae78be716cd9 | -10.907 | -43.8433 | 2026-09-30 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 156352bf-7e0b-30be-990f-c82ec950de69 | -12.5135 | -43.0943 | 2026-09-30 18:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 221.1 |
| 7acce552-6017-32ab-8604-faef101b1cd7 | -13.384 | -43.9895 | 2026-09-30 18:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 81b4fcce-191b-31da-936e-84d53d0c7c0b | -11.2566 | -43.5331 | 2026-09-30 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 422379a5-9261-36a8-b1e1-ba433f04a5ab | 1.8586 | -55.6241 | 2026-09-30 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| eace4b4b-14b1-3785-83b6-e27d5391a479 | -15.1214 | -41.3652 | 2026-09-30 18:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 115.0 |
| 06243921-2bf7-360d-83a2-222fd6979d81 | -13.1037 | -47.462 | 2026-09-30 18:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 98d8714c-1673-3565-b7ef-ae248e541f77 | -11.6986 | -43.4654 | 2026-09-30 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 82592ce0-71e1-3402-a828-798734644f1f | -10.9653 | -47.2845 | 2026-09-30 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| b7eb8538-cb06-3fb2-8ee6-197b37b53039 | -7.2721 | -72.7177 | 2026-09-30 18:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 3881827f-e1ff-36b0-b0ae-65e19eb0503b | -0.6732 | -49.2591 | 2026-09-30 18:40:00 | GOES-19 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6b48b0ac-2bc8-3bbe-a1ec-359fb39fb230 | -10.7112 | -45.3075 | 2026-09-30 18:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 093a0ec9-d38f-38a5-a672-985e4eadd4d6 | -13.3835 | -44.0132 | 2026-09-30 18:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| c7a064b6-8b20-39b4-82e4-8f04a9972462 | 1.8586 | -55.6439 | 2026-09-30 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| cbc2ef8d-671c-3f66-84a4-3b1b6d068dce | -3.2888 | -42.8795 | 2026-09-30 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| d8898dc8-ec56-3220-91d2-8b72fc84d630 | -13.8685 | -43.9975 | 2026-09-30 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| a98acbfd-ee65-3f88-af9e-3adb333c5b67 | -0.6733 | -49.2379 | 2026-09-30 18:40:00 | GOES-19 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6c17bdd2-d098-33df-aaa1-3fb5406cdd28 | 1.8403 | -55.6442 | 2026-09-30 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 981ffbfc-f033-3817-9b6c-256207ddd04e | -6.1894 | -44.8472 | 2026-09-30 18:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7f53cf84-453b-3ec4-9a6b-4e3651c8cbb9 | -13.0017 | -44.7357 | 2026-09-30 18:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| eb45fc99-5dd4-3133-bf16-80cc635e1cf9 | 1.9793 | -50.84 | 2026-09-30 18:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d4ea79a0-5ef4-3f01-809d-a35ae144cb3f | 1.8036 | -55.6447 | 2026-09-30 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1099b867-0d74-3bd0-a3f1-1226e08d3235 | -11.699 | -43.4416 | 2026-09-30 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 7e08ed88-c686-393e-9195-d989c23c5cc9 | -2.482 | -49.2509 | 2026-09-30 18:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f05ff950-c6f3-3986-adeb-71436399fc29 | 1.8037 | -55.6249 | 2026-09-30 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 1aa45c8f-7553-3713-89af-86286a92c355 | -15.1348 | -44.0412 | 2026-09-30 18:40:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 218.9 |


