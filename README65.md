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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4aa7bea-950f-3d13-8168-831a069296bb | -12.37286 | -46.5616 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72712851-112f-3e63-96ba-9d754c5dd7ee | -12.70632 | -47.87987 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfddda40-b4ee-3d56-b97e-8c8d171e86ed | -11.55972 | -52.10935 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a1d758d-38dd-3a0f-abd9-57bd10d4fc97 | -9.07816 | -65.72489 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 855a4fca-5f3f-3d74-a050-78f480a7ed7d | -9.16967 | -59.5373 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 95b9da6b-57c5-3504-93b5-a23276323cca | -6.82085 | -59.43091 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4180ce3a-404e-3c31-84d5-3947336235b5 | -9.16698 | -59.5162 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6ab7013-d882-3a04-a23d-52f53f0ac76d | -11.54979 | -52.10775 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a677348-1677-314e-ae5f-a99c06e64bbf | -8.34437 | -62.94252 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 919e5f21-8a5f-392f-b212-cff1728ce966 | -12.72979 | -48.16403 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0f6678d-2e47-3711-88fb-1c8c07112a4c | -9.16186 | -60.77354 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ccbd254-599a-36eb-9b45-8802332f1e17 | -11.56745 | -52.125 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c4105a2-576f-34f9-9540-5e5ac3f2723b | -8.54694 | -62.63855 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95563904-9fa2-3f9b-8417-e2ac29aa7c3f | -10.3873 | -57.6922 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 519d11bd-e67c-3b50-9c94-01db125f64a7 | -11.29451 | -53.96004 | 2025-08-26 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c25958-c8fe-3ddc-ac8b-a84b169e037d | -12.76236 | -48.13939 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 53bf6fc8-5855-3b04-bb7a-4c32345b4f79 | -14.39884 | -51.94441 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62ee0c14-1182-38f2-bdd7-44b255d09340 | -13.4091 | -46.89026 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 478279d2-ca59-3c52-a291-07014c7bc0ce | -12.74909 | -48.16673 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 85bd5916-f4e0-3137-a170-dd87c127d48a | -9.57714 | -55.37408 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83c7d6ae-65cc-3876-aa47-b5cafb63ba1f | -13.60893 | -48.17294 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9931a865-846f-3682-8382-eb2bca27bd8a | -7.36101 | -59.66718 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ab0ea2e-c9fb-3a98-a44f-b36e648002ba | -11.55862 | -52.11637 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef790490-852c-301f-9b58-d7e49c5831d8 | -10.10489 | -57.76662 | 2025-08-26 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bf2a3d7-a36a-372d-9f62-82582b878d8b | -13.64986 | -45.70447 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2afb9434-2a4d-3886-97a7-54f4a9f011f6 | -11.56579 | -52.11393 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 981fdb82-5ba2-3fcc-8979-56afe694bd77 | -9.15811 | -59.54633 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8e08771b-efcf-39bd-b0a2-86a0be8bf0e8 | -15.10778 | -48.63255 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60eb09c9-343e-36ac-9663-6b5aeccbc18d | -15.14154 | -48.6733 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ececd618-4989-3cf2-a17e-5929307ed9e5 | -8.85373 | -62.44186 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 18861d14-8924-3965-85ea-356af8b7ff5c | -7.64979 | -63.52829 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 920fb13c-dc68-32af-bbdc-b1e69460df58 | -13.41596 | -46.90312 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9433113b-d65d-3604-abb9-0f56dbb18dd1 | -10.14975 | -48.88486 | 2025-08-26 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ee5673f-3e88-3b92-b553-4dcff0f9884e | -9.17825 | -59.51672 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b6dbdc4-367d-3ce0-a817-1dbc4f4abcc5 | -9.17769 | -59.45775 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8d1f3452-bce9-3b17-8938-d15ab2e3398a | -12.41884 | -43.49163 | 2025-08-26 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18a8204d-4641-3801-a4f1-7ab9904e7bd7 | -9.25014 | -56.90702 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7ed98a7-d295-3fca-88ce-8717cb5917f4 | -9.17083 | -59.52242 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7fd7004-89cd-37ae-b48d-704008841f71 | -7.37156 | -64.36412 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5a11ef07-5d8f-35fe-9b21-3de6f05bc5c8 | -13.61094 | -48.15606 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22141ee5-0093-3ef2-b690-23bc601fe27f | -14.2475 | -48.03481 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 912b8a13-24af-3640-82f3-4a2e7b45acb1 | -11.53434 | -52.11966 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7427ee0-c2a4-3ea2-989e-4fbf9b7c66f6 | -11.55365 | -52.12637 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70359227-f73e-33bf-a299-6c830c941e39 | -10.01711 | -62.39258 | 2025-08-26 04:46:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46defd1a-5ac5-35fe-bfd4-3f259e3001ea | -10.39567 | -57.69369 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a660bdef-e681-3288-a71a-d4afc57ba131 | -11.53986 | -52.12774 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 3ebd6dd1-6ea6-3033-b47d-7f89ccea6197 | -13.60775 | -48.1523 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 811eaf09-5b95-343d-8db4-7bcadc693da0 | -15.31999 | -53.84183 | 2025-08-26 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab8268fa-31bf-3f76-ae97-30159b12455e | -12.73331 | -48.1395 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd7b2603-88cd-3709-a6d2-885ba5ec2a0b | -14.28259 | -49.12971 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42e0ff9f-4d43-3592-ab8d-b410a72f886d | -8.85137 | -62.45473 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fc4fc48b-c641-3c95-9f22-4cb33c94a283 | -13.40857 | -46.89424 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f875ce7-f918-3985-9322-63c4981b78c7 | -13.64393 | -49.0069 | 2025-08-26 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5102e4c1-5b00-37b0-bc48-15b39d745e43 | -9.02239 | -65.72884 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d96bc52-19b2-33c7-a3b5-d7d0a67d5959 | -9.23693 | -60.92591 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b487be-deb0-37ba-ac7b-5a1876de6865 | -12.70422 | -47.89508 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f26183a-800c-3ff0-b78b-6117154e16e2 | -9.63821 | -59.6372 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a1824c1c-925c-30c7-8b6e-3fe7ba725930 | -12.74479 | -48.15256 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0232fe7-ac6a-3f24-905c-29446ba3194b | -8.55624 | -62.62187 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e073c7bd-f84e-36fc-8ae0-3900dd0b235b | -13.05902 | -46.32481 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d669aac1-0f34-31be-add6-91eb2269cbde | -9.18805 | -59.62017 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb7d3910-acb5-3235-865b-7523a3fa2cb8 | -8.55374 | -62.63525 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c57b3cfb-3aab-3a16-8f01-eee099ec7bed | -11.50454 | -52.13643 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d0ad26c9-6fd6-3a66-ba9b-c372927b3d8e | -15.03267 | -48.68064 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 832a3eeb-e337-3e6c-b01e-33eec9552f67 | -9.0793 | -62.66787 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 236fa527-516e-3372-ae81-4c557435ba51 | -12.74735 | -48.16254 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3d36c427-31d0-34e9-87b2-d77158c5b5aa | -11.15471 | -44.76332 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 67454c3e-3528-34ac-834a-4bdfeb3268e3 | -13.44192 | -47.00264 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd9a0d60-5631-353a-80d8-91344b23ca56 | -6.82442 | -58.96904 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5f6e1897-af16-3c56-be3c-7bd24be1defa | -9.15905 | -59.54095 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 99944ec4-6340-35b4-b90b-635e0e633be8 | -13.41179 | -46.90222 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b04206-6e77-3fc2-9bbf-0f95d9146e27 | -9.79411 | -64.2607 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a6307b0-2f73-3172-963e-ad0945e0d2ed | -11.62678 | -46.21848 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57e9a0b0-ca49-3a4f-8cff-52ae427ecacd | -10.25181 | -59.10654 | 2025-08-26 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca60ad80-fd9d-3127-906d-714b359ad955 | -10.44198 | -47.1812 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5922102e-cdcc-3ce9-b3ad-fcdefeac6d8e | -12.66851 | -47.86371 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6637e68-de8a-3d6b-83d6-ce9919b2c66d | -13.42011 | -46.90422 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e9ef269-1627-3b60-810c-c34105bb4add | -11.56414 | -52.10287 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a059ade5-1a48-33e9-8726-afb2d6cbf01c | -9.16682 | -60.77301 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c893b15-1ba9-38de-85b8-78fd76c597c6 | -13.35711 | -54.39348 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 411bf56b-c8cd-32d4-b19f-8d975a17dcf2 | -8.85524 | -62.45563 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7addb61a-80c7-3108-8002-a59c48da20a3 | -10.76502 | -47.069 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee595693-759f-3bce-953e-0f642ee63867 | -11.15186 | -44.77234 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fa47abd1-6755-35fb-a03d-93254649ad1a | -12.75115 | -48.16355 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 386fbf2e-8691-37f3-a409-307925c960bd | -11.56414 | -52.12447 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a69a62f2-5697-334b-ad60-dce224f170b3 | -10.74347 | -47.07659 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b6575b95-2c5a-3671-b2d5-d808c4386f58 | -10.02341 | -51.07883 | 2025-08-26 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77e57dad-61e6-354c-8423-c451665ea376 | -11.13783 | -46.33458 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f050fded-413f-3192-945e-75e46e91ab40 | -7.38059 | -64.35331 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 34807bac-db01-3bd9-8cc5-c727151799f1 | -9.16201 | -59.55256 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0170cb61-b68b-3dd4-95e6-30d8a25f6124 | -6.78306 | -59.67292 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0b49c9c-7d6b-3efb-9cda-26241e516748 | -9.06125 | -49.55451 | 2025-08-26 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f15ee7cc-e483-3a1f-84a7-0bb87b2dbe2b | -10.81324 | -46.37543 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f1f7288-05ea-3549-ac25-ea6da25c7506 | -15.1764 | -48.18941 | 2025-08-26 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91f50a50-375c-37e2-98f4-81dc812cd8f1 | -9.58081 | -55.37471 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4405b89d-1301-3c8d-919a-108a262538fa | -11.53765 | -52.12019 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c38d78b2-2efb-3a24-beed-3281e445f826 | -11.54703 | -52.1037 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f293664-696f-3b1b-bb03-d7ab2b98471b | -14.3587 | -51.91573 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60528627-3d1b-39df-b79b-80b59fd877ac | -8.86712 | -52.04122 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efc81df6-5f42-3543-a060-03bb24045f66 | -11.03156 | -49.14166 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README66.md)
