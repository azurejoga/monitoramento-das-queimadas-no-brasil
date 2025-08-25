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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 273513dd-8f8f-3b6c-83c6-15f82004b20b | -8.86969 | -62.4584 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1e743863-c579-34dd-b8ab-e9b846e60ed6 | -9.49185 | -58.93417 | 2025-08-25 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7be98c80-0537-3782-9f56-8ffbbf4037e0 | -11.61317 | -46.23875 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0390010-ffd6-3ece-9fa0-0ac4440ad650 | -10.02409 | -51.07478 | 2025-08-25 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7cf0125-932f-3032-a751-49a99354b1d2 | -5.42465 | -60.16526 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a59cd081-3234-35ab-b220-4054ee42ac6b | -8.89542 | -62.46298 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9979d11-fcd1-3999-9bff-20d9d7bcef22 | -6.62651 | -58.54735 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f096b619-4ee8-3773-9212-f993d75ea713 | -10.72884 | -47.11244 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1123bedd-c16b-32e1-8386-97d4a211b323 | -7.31428 | -59.61197 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc343a41-24e9-33c5-8539-a15e214ec351 | -8.22789 | -61.39075 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 893fdd44-f6ca-3e92-8535-3c6ef423f8c3 | -5.79761 | -59.22195 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e018370a-bc49-30d1-9b4e-f614d5ceb3c1 | -9.19374 | -60.79243 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88157d96-b914-3543-90d7-9023eeef6c16 | -9.19418 | -59.4646 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b803b0b-fe15-35ca-90f7-15d3fba6c3b5 | -5.44549 | -60.18597 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a62b627c-36c4-3e57-ac69-8b533b894c2e | -8.61039 | -62.64746 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e043874d-4e83-33af-a6a7-d9c9826acc2d | -11.4614 | -55.46966 | 2025-08-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e4a034c3-da26-334b-9bd7-539d89d89fff | -12.68652 | -47.83223 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35a9c4f2-8f02-38f9-8f66-1a6839953580 | -10.28308 | -60.55077 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbd5dec9-5a44-3142-b0dc-089e3cfb9d00 | -9.20419 | -60.92592 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 417b131e-ec28-3824-87db-d46f9bd0c757 | -9.13013 | -60.73486 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 823dd3d0-7f2e-378c-a658-1767b32c6eea | -8.62644 | -62.63287 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a966af5d-719e-3fb8-82a6-784c90c6a56e | -11.64055 | -46.21104 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49059183-5956-37d4-b969-87e57b39874a | -8.5865 | -62.63009 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abbf22ec-1ae0-30e9-873e-3f79132dc5e8 | -7.91299 | -63.06994 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aff9c8e8-1d3e-3e1f-90fe-9f86406cc6f1 | -11.17181 | -55.02665 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c28fef0e-4138-3ba7-b5da-6eacb990a131 | -9.05996 | -65.72483 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c5b2393-38df-349f-a5aa-84aa55074e38 | -8.87258 | -62.39177 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5335597-44e2-39fc-84d0-fbe4236303f9 | -8.9856 | -65.42464 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 50b9254a-178b-397e-9730-1507aab49d3e | -8.92746 | -62.43079 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 292f7a22-4464-3308-9c74-6ab341de0aa6 | -5.80129 | -59.22252 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cfbe353-8382-3444-8d71-b7427dab3a66 | -8.23339 | -61.43224 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09930104-147d-314d-a453-3a6c847995af | -8.61425 | -62.60019 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 863eb0a7-d97f-33c7-add9-8b597d44feb4 | -9.70798 | -54.98509 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d0593c4-5df8-3abc-b09d-37fba9f65b00 | -7.9002 | -63.06276 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6f44a501-07f4-31f1-ab9c-7c99db88be87 | -8.50073 | -63.87104 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9ed11726-330d-32cd-869c-eb986784b919 | -9.2489 | -60.48745 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cae5a40-2359-362b-a44c-8873e1a7341d | -8.12516 | -62.87044 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22e6a838-0f73-3019-b11a-6e16e401d5e6 | -9.50396 | -56.1036 | 2025-08-25 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47470261-a1ee-3a5e-83e2-70d8a21e9835 | -10.2577 | -59.10161 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31f5fd55-4556-302e-8fa2-709aff6ee201 | -9.80329 | -61.20916 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0b4e9a5-6fde-3dcf-b8ee-375e4a5bff0f | -8.9032 | -62.41814 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19ab9a99-be2c-3056-9270-773b77886feb | -9.62936 | -63.09899 | 2025-08-25 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 067415f5-2a1d-31f4-a250-2d81ce468294 | -10.61263 | -55.04568 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b815f954-6747-30ff-8ea3-1ed6af966934 | -11.27658 | -44.99139 | 2025-08-25 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ac37adf-909d-32ac-afa4-6615161503a3 | -8.89684 | -62.45482 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89717890-e328-3fb0-82a2-4bbeb154546b | -9.14635 | -60.76933 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71967732-47bb-34b2-a906-df1bb26e883e | -8.21982 | -61.38932 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bcfc92c-3187-37c1-866f-3b467f1912d1 | -10.71596 | -47.12574 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8eaf7bfa-1023-36a6-ae83-eb8206320b5b | -9.24666 | -59.6252 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85f5fe58-b14e-3cb8-832d-1babd02d890e | -9.01876 | -65.39099 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 357eaa54-c0d9-357c-a8fe-618442ab72e2 | -5.4268 | -60.1778 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3a8324bb-e85c-3104-a385-941769754f67 | -9.52167 | -60.52798 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7923b325-f636-3c3c-9ddc-5c3da3cce7ba | -9.22111 | -59.71123 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caf679e1-5383-3870-b375-3a6de58b22a7 | -9.22605 | -59.68185 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 561c6b01-0e2a-3c2b-8194-f46f9bd03e2b | -10.7219 | -47.12321 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 481003ed-69d1-3459-a582-df1497f00ab7 | -8.06476 | -49.68112 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cedc875-16f3-36ab-815d-977216196c3f | -8.2206 | -47.17686 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3d01254-47a2-3690-8382-cdc84b432dee | -9.13721 | -60.3439 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdd0a1d3-cba2-316f-9ecd-fe870537ea69 | -9.06591 | -65.72247 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d628143-9be3-38dc-b6f5-a06885954acc | -5.80739 | -59.22617 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b61c8217-dece-3007-8f09-200d43e9ae95 | -11.20003 | -48.47172 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 303a8225-ba72-37dc-baef-aaf4df385ffc | -5.75047 | -51.70398 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58b06b35-4852-3ffd-9336-9b4ba98ea449 | -11.86312 | -45.118 | 2025-08-25 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93294f81-b1c1-39fa-8e73-dc09e824b206 | -9.00019 | -65.40408 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 39c77cee-9fad-3e90-83d1-4f15f9fa648d | -9.19651 | -60.91755 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d24c30-322b-394d-a941-3ab5ebe63716 | -8.90183 | -62.45152 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d50ad581-16cd-37fc-80dd-cbbb95209704 | -8.61065 | -62.5952 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10c1fbbb-cdfb-3482-9e2a-f64b2e55e8cf | -6.78672 | -59.65559 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a7f252c-0b30-3de8-ab91-723bf463e315 | -8.38555 | -44.94662 | 2025-08-25 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec23b6a5-a49f-3d34-a545-6bb12891a468 | -7.62025 | -62.72465 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 15f7c730-0b99-3038-9ca8-b5fc470dec48 | -5.74838 | -51.71772 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9276f678-dcdd-3282-8447-00306a4b2004 | -8.92725 | -60.71985 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ded78ae-2810-30db-9aaf-f94adea8b075 | -8.11669 | -62.88123 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c335d48-3dbb-3007-b226-70c5d34d4fff | -8.06414 | -49.68554 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33cfc6a2-1eb5-3fc6-891c-70f18cb688c8 | -8.67769 | -62.88012 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbc1ecda-87b2-3401-8d46-fec43596a95d | -4.9573 | -55.81653 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b63755b-a0e6-3739-bafb-6a42c627b16c | -9.1549 | -59.45798 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2ee4bd2-c4fb-34e8-a8c2-b4650f0df118 | -5.74146 | -57.57928 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff96149d-36ed-3ff0-adb9-ee3ce874f4b0 | -10.24128 | -59.66374 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89294842-1407-3679-b3e4-a087dfae9d26 | -7.53424 | -50.53211 | 2025-08-25 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3344e234-9bad-3860-912a-d75af956e4d0 | -7.81269 | -61.32758 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4de23ec-aa40-3b23-9ce5-763c745bfe25 | -8.87898 | -62.45584 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2bb8ff5-3000-35c3-ae85-add0bea3b18f | -9.16115 | -60.82142 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 105c30d4-6e77-35b0-a7be-655c46465c76 | -9.16233 | -59.50151 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b200b14-799d-355c-9644-f93720b99a1c | -9.18752 | -59.61655 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14d966e7-bec4-3cd0-80fd-532c7d7e59a0 | -10.70613 | -50.54903 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9539a3f-9af9-3d1f-90ee-63d6ab3770a2 | -8.88398 | -62.45253 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 950ba632-eb98-3157-8cb0-df2c79aefff7 | -10.61548 | -55.0499 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cea9f2a-0e93-31e7-bb49-28cb1768635e | -8.99261 | -65.41593 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b0363f5-04e1-3b6a-9b8e-df655bb994f7 | -8.87041 | -62.45433 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8de9d036-aa47-32b1-8a47-3beee5841e26 | -12.29552 | -49.14086 | 2025-08-25 05:04:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c19c348c-cc0d-3c7b-8fd9-4ed9ccdd5f4d | -8.21959 | -61.41522 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b6177c8-a9db-3fc0-88ca-17eac9a0311b | -11.03039 | -59.17414 | 2025-08-25 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f249537-6b55-395c-99c2-9c0302c875d2 | -9.57945 | -55.37337 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a673f693-1fe5-35b5-a6da-a4bd5e7b18d1 | -12.74644 | -48.13137 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc78a6ba-6ad6-37d0-89f5-e88c3b9843e5 | -9.68438 | -48.33757 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3940610-996e-3983-bfc4-439886dcc1f1 | -6.78878 | -58.64135 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c405b8f4-7a15-3e4f-b638-2296ce6905fb | -6.63132 | -58.53999 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff436762-8466-3ce7-ae46-8504c6fc00e5 | -8.21151 | -61.41376 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 100d7aa3-bc2a-3ccf-8418-949fa1c2634d | -9.15999 | -59.47147 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README71.md)
