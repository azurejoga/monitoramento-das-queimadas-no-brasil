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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 095184e4-fe1c-3813-91c8-17a8636bdb4e | -3.85911 | -45.10886 | 2024-10-27 04:23:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6002b3d-9ee6-33ca-802c-230f4568dd71 | -3.85857 | -45.11232 | 2024-10-27 04:23:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f6aab22-edf3-32f8-ad5e-61c6ad5d1f86 | -3.78968 | -44.96669 | 2024-10-27 04:23:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bdbcc07-42fb-36c6-860c-6d58a379aca0 | -4.42542 | -45.9598 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c52612-af08-3e22-82cb-ed83ad31fb79 | -4.35542 | -45.84313 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2045545e-48f2-3b3f-ab87-11d5ba8b6e96 | -4.35488 | -45.84657 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ead7f81d-12c2-3bf7-9412-e7f3f0db0b79 | -4.35212 | -45.84261 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff4c20e4-b43e-3531-af1d-4f2fbb87d4b5 | -4.35158 | -45.84605 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bb90adf-b5f0-3399-9425-889ec7aba167 | -4.34828 | -45.84554 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0b1095a-ee4b-3893-90b1-9ba62dde3f06 | -4.34552 | -45.84158 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 851b8255-c652-3d52-a33d-2c24a3eba507 | -4.34498 | -45.84502 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dbe1386-7666-3d3a-9465-435c597d2fea | -4.28232 | -46.07124 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 375ed8c4-a97f-3fc5-b7cd-6184ee3cd69b | -4.06175 | -46.02634 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e324727f-23db-376e-9330-427c7d1cf41e | -4.05917 | -45.67343 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebca6590-b460-38a7-8a9a-770e50267d70 | -4.05863 | -45.67686 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bcb0d7e-51bb-3ad0-9ee6-5ef9b8c8bc7c | -4.05845 | -46.02583 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5f88574-1ef2-3813-860f-b4a632f21dc3 | -4.05809 | -45.6803 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43f41442-3577-3d20-95d5-899537480057 | -4.05568 | -46.02188 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd1d7a8e-36e6-30eb-982d-00666dd2198c | -4.05533 | -45.67635 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b300b868-4574-397c-a0bf-910cd4b54a16 | -4.05479 | -45.67979 | 2024-10-27 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9081ede-5c1b-31c5-9473-ed01e6ef8c12 | -3.9375 | -46.03826 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a403b933-7459-377a-8260-a9aa6db3584d | -3.93695 | -46.04171 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2489fd7-9731-3934-adda-4f981ec6866d | -3.93419 | -46.03775 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10b5e43b-2dcd-31be-a77b-fd3074452c57 | -3.93089 | -46.03723 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfebd421-ad80-3eda-b091-96689afaaaa6 | -3.92704 | -46.04016 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c95bb2b-a41e-383d-a9e1-02ed029e54c0 | -3.72374 | -46.03612 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2172a9c3-50d6-313d-8e48-30501ae5ac36 | -3.67752 | -45.9407 | 2024-10-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae9aaf90-9ae7-37a0-be35-270e926f0ebe | -3.67627 | -45.88414 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e7d4903-e23f-3901-acaf-b5ea70c3245e | -3.67296 | -45.88362 | 2024-10-27 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6620988-7514-340c-8044-7ad088108538 | -5.97834 | -45.37104 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a5e8d47-62a4-3b78-a98e-a0d63fc2884f | -5.9778 | -45.37454 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e992c58-6e3c-388a-9692-67103cb435a3 | -6.33422 | -46.3313 | 2024-10-27 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ffdc2a5-39c7-3494-b549-0fb38884b283 | -6.33368 | -46.33474 | 2024-10-27 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64db009d-5e24-3be6-ac32-b02114be323a | -6.33038 | -46.33423 | 2024-10-27 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e623a42-4191-3bd3-ba01-36172213bcb4 | -6.06984 | -46.34998 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff0a5864-b844-3a88-864f-549bc4a63bd6 | -6.04508 | -46.35669 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c6d3330-8065-38f7-bf9f-ac0c457e0aff | -5.86776 | -46.14472 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 052252ed-737b-3038-ae76-eba6ba4df498 | -5.84268 | -46.23966 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db1e9cb4-dc45-3301-ab52-4508b0da3c2e | -5.70986 | -45.52565 | 2024-10-27 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19c5de9e-a22c-39a1-9e16-7634246e12f0 | -5.66593 | -45.80593 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2822b70c-c296-3dfc-9550-731a57738bdd | -5.64877 | -46.28352 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a24b451a-0e8e-31da-8610-c2a5a0a15605 | -5.64823 | -46.28696 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b13b4efa-dcc4-3359-b2c5-05602f52baf9 | -5.61728 | -46.2256 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f5826ae-a8df-39b6-b7fd-615556c09163 | -5.44253 | -45.88714 | 2024-10-27 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bdb38f6-3910-3d68-b4a9-4466acabd801 | -5.35833 | -45.88458 | 2024-10-27 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7af3d85f-5c24-3f37-b593-490f40423c08 | -5.35764 | -46.25493 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dded72dd-1f14-34df-8993-05cc023f910e | -5.27278 | -45.95198 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4f72b22-d1f8-363a-8c75-fbde38fc47d5 | -5.21524 | -45.7989 | 2024-10-27 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36f531c8-56dd-3297-8213-53c020d98db4 | -5.21193 | -45.79839 | 2024-10-27 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3db349bd-0bb8-3284-a1d8-27454a6913fb | -5.20124 | -45.54224 | 2024-10-27 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ed125cf-bf44-3ded-aeec-a697a6a21686 | -5.19848 | -45.53826 | 2024-10-27 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2094cb45-a2c3-3974-bbb2-1b38742fa1c9 | -5.19794 | -45.54172 | 2024-10-27 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8265fa36-7e1f-393e-8912-f6bec7dc5ae6 | -5.19517 | -45.53774 | 2024-10-27 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90d557b3-179c-3f1e-bb62-53349a9fae29 | -5.19032 | -46.15121 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 734dfebc-f436-3852-bd18-8a5973e264c4 | -5.14221 | -46.04848 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b10fbb1-36d5-3be0-a0e4-b40021ae89a4 | -5.08916 | -46.17063 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b3601dd-7594-3664-81b3-db8e1c55b98f | -5.06872 | -46.10357 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e27157f2-60fe-3d5c-9b11-c43e1a1a5329 | -5.06596 | -46.09961 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c84d1c7f-2454-3302-80e5-feefa8701bf7 | -5.06542 | -46.10305 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e107bd7d-9f73-3402-8956-1d3d41e54304 | -5.4101 | -45.40015 | 2024-10-27 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d152bf5-0422-3646-a53a-0b7f4e8242fc | -5.40955 | -45.40363 | 2024-10-27 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 306d9ab6-9619-36f3-8af4-74bcc73088b3 | -5.40623 | -45.40313 | 2024-10-27 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a398a867-56a6-30e8-9c3f-9b6bac54d4a4 | -6.2327 | -46.15681 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29889171-11f1-3dc7-b0ac-1359522cd970 | -6.18819 | -46.18164 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 908c7f8c-c048-3b1a-a785-a5d27856e0f0 | -6.18177 | -45.43868 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d476c7a8-bc90-318c-a46f-ff822819081b | -6.18123 | -45.44217 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92a70879-0c95-3010-b6b3-179ebb6e1506 | -6.17791 | -45.44166 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 86260efe-d441-3a9c-bba5-fc5692ec1b67 | -6.17737 | -45.44514 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf829af9-731c-3d27-a6f2-d01fd262f527 | -6.17459 | -45.44113 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5bb0706f-5f93-3e24-82e7-8861fd71916e | -6.17405 | -45.44462 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6df45107-fcfc-3f40-982b-c28cf1ece38c | -6.10513 | -46.14703 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ee86efd-2352-38db-8a37-1e46409f89d6 | -6.0841 | -45.60895 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4927e717-ae5d-368d-b055-10fed9664ccd | -5.99319 | -45.97402 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf670ec4-d457-3020-98a8-f08b20d79ca4 | -5.99097 | -45.96661 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f1987d9-9fb7-3cf9-9d05-a55a4be89b5a | -5.98767 | -45.96609 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b671479-0d58-3abb-8121-e18fe73e5b69 | -5.98544 | -45.95868 | 2024-10-27 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75775bb9-5d57-3d38-9dd5-d8d0d3494843 | -7.15161 | -46.55661 | 2024-10-27 04:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef2f0635-7506-3a70-9080-e313d8c9aa0e | -7.12262 | -46.37502 | 2024-10-27 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e345a86c-71d1-36e5-bf27-aaeddaa9b838 | -7.1204 | -46.36759 | 2024-10-27 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 196339bd-cf19-3fc1-9b61-33b061bff085 | -7.11986 | -46.37105 | 2024-10-27 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6da96be7-e79a-38f7-9795-bfcba708e1af | -7.10629 | -46.45745 | 2024-10-27 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2408c9dc-11d6-3a09-bd37-8c2fe8e7124f | -7.1008 | -46.33966 | 2024-10-27 04:23:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63fda4eb-f3f6-337f-af2b-bad1e37a1448 | -6.95558 | -46.31291 | 2024-10-27 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0eb26cca-f52c-3d2f-a035-05dfaba6a9ac | -6.95124 | -46.34055 | 2024-10-27 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32914831-0aaf-3251-9d22-884fc7bf30e2 | -6.92752 | -46.31912 | 2024-10-27 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 632f8530-839c-38c6-85fb-4427709e5938 | -7.20432 | -45.56876 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 164d495a-9647-333f-91b2-8ed291879e89 | -7.09306 | -45.29823 | 2024-10-27 04:23:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89f8225a-f57e-39b0-aa86-6281a78bf1e3 | -7.07319 | -45.75602 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a92501c1-44b1-348f-ac3a-88b27e57d5ac | -6.89432 | -45.57458 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c41eaee-f032-3952-b5cf-164bb125e337 | -6.8732 | -45.88518 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d96c3c61-1cce-35ee-a13f-9cef71dee016 | -1.66782 | -46.55051 | 2024-10-27 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4b02609-b40c-337c-acf3-f73a23d718b7 | -6.85963 | -45.88336 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31c9ebcb-2ef6-3a93-b1fe-7cfcb224754e | -6.85796 | -45.87241 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e12b43be-f952-3c9d-9ac0-1421641dce7a | -6.84748 | -45.87435 | 2024-10-27 04:23:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f83162c-672d-3f23-b776-8aa63ed451f7 | -7.27632 | -46.06625 | 2024-10-27 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1824257-8187-3fbc-b276-3d341ee11240 | -7.25787 | -46.07367 | 2024-10-27 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00a9283c-e016-3023-8aee-b039e8233e84 | -7.25733 | -46.07714 | 2024-10-27 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ccefc13-bff2-3928-a5dd-2353edd3b8dd | -7.23798 | -46.04922 | 2024-10-27 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c954ed5e-502f-3f75-83ff-441d9e245144 | -7.23743 | -46.05269 | 2024-10-27 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0238727d-0bae-3ca2-a5b4-bcbf67ff51f8 | -7.23467 | -46.04871 | 2024-10-27 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README43.md)
