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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f99e88b-7bee-3425-92ea-405fde76de74 | -13.5502 | -46.2844 | 2026-08-11 07:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| bfbf6558-bf4d-3935-83a4-47f3d87e4242 | -13.5507 | -46.2615 | 2026-08-11 07:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 3f1cd08b-8ad9-3e6a-bcc5-df88fc5fddf6 | -13.5701 | -46.2584 | 2026-08-11 07:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 5e6dd8f5-6531-3596-8c4e-ef60308fbf9a | -13.5696 | -46.2813 | 2026-08-11 07:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 184.9 |
| d91c11cb-b973-3635-b220-bc490fa1d635 | -6.24552 | -55.61897 | 2026-08-11 07:14:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 24148d97-e274-33c8-973c-af4b50ab80af | -2.95902 | -49.25839 | 2026-08-11 07:14:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 8f79849b-b765-3110-ad6f-16cbc91432bb | -13.55 | -46.28 | 2026-08-11 07:15:00 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e2075c8-0bcd-3c7c-b464-6007fb544b50 | -13.58 | -46.29 | 2026-08-11 07:15:00 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 329e483f-f493-3c93-bcef-4ab8ae924bd5 | -8.95648 | -60.53235 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| d1ce25d3-9e86-35c4-adea-64cc4741e122 | -8.96147 | -60.54004 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c0df971a-5042-370e-8ae0-bd4d0f6e5009 | -8.95445 | -60.54517 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9377adf8-a7e7-3d89-8240-eb5e16fba282 | -8.95105 | -60.53838 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 0e13009f-8e3b-3b15-9660-f34b73958cd9 | -8.95244 | -60.5579 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| d040951d-f35d-3e0d-9e1b-c20de3f7f245 | -14.11478 | -54.0009 | 2026-08-11 07:16:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 47b1c9b8-802f-3af3-bf30-932aad3c8f61 | -9.4701 | -60.52409 | 2026-08-11 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 962044f5-04f6-3793-9dff-dcd0be9e80fb | -8.94607 | -60.53067 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 64259ca2-e6dd-3531-8627-94e90f2cb512 | -8.94894 | -60.55112 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 0b61ae22-8039-36f6-813e-b771a0fe0156 | -8.95937 | -60.55276 | 2026-08-11 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9e5d7e8e-ca40-36e6-8916-4829ee1202a6 | -11.6414 | -51.6453 | 2026-08-11 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 3ed1091b-560d-3208-b43e-93fd678598a3 | -13.5502 | -46.2844 | 2026-08-11 07:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| aba5dd27-9739-3287-b031-ba6d5cbc4324 | -13.5701 | -46.2584 | 2026-08-11 07:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 73a38de7-2975-3650-9ea9-9ed37155b403 | -11.6604 | -51.6432 | 2026-08-11 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 444159c0-e719-3cee-8e18-570873ce9243 | -13.5696 | -46.2813 | 2026-08-11 07:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b31d6787-c353-3c98-8e41-0df8a8bf2cf6 | -9.3909 | -47.4656 | 2026-08-11 07:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 2b293560-17de-3d06-a8a9-bf611200f2fe | -13.5696 | -46.2813 | 2026-08-11 07:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| dda9038c-7765-3b1f-ad01-f70a8cfebed9 | -8.9602 | -60.4973 | 2026-08-11 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3c80c136-ead7-3c67-a3cc-aac2153abbb6 | -8.9414 | -60.5367 | 2026-08-11 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 72c19484-7967-32b5-b450-3cad0ff7683f | -8.9416 | -60.4982 | 2026-08-11 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2d553a16-3156-32bc-a758-86af376de5f9 | -9.3909 | -47.4656 | 2026-08-11 07:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f8f492c7-f59a-3513-8442-a8749607d0bd | -8.9415 | -60.5174 | 2026-08-11 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fb710b64-eaac-3e38-b76e-57bd53e07b9c | -8.9601 | -60.5165 | 2026-08-11 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 0bc32958-eba9-388c-b1de-783bb43ad61f | -8.9415 | -60.5174 | 2026-08-11 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f5ac6aac-4d74-3fb8-b16d-1df875889531 | -8.9416 | -60.4982 | 2026-08-11 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0e467ed2-0f55-394e-bb23-859cbd668eab | -8.9414 | -60.5367 | 2026-08-11 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 930a5b2a-548a-3420-a0f1-b6b23c7bd9e5 | -9.3909 | -47.4656 | 2026-08-11 07:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1c3529fd-13f3-3b43-8c7f-e29c9629c9fc | -8.96 | -60.5358 | 2026-08-11 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| c25dd6df-ed86-328b-b25e-673349012b24 | -8.9598 | -60.555 | 2026-08-11 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 81a38135-5aca-305d-9b73-89fd8e6d9fda | -8.9601 | -60.5165 | 2026-08-11 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ab9afaf8-85fb-3825-8fd8-3334648c718f | -10.4234 | -46.7033 | 2026-08-11 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a51dc49d-25b7-3fda-80c1-f48a0f1c9fef | -10.4237 | -46.6809 | 2026-08-11 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7e9c7c00-f667-39c5-b1cf-09c27ba308db | -8.9414 | -60.5367 | 2026-08-11 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 654c1ca2-7e94-3656-b852-100b006c3eaf | -8.9601 | -60.5165 | 2026-08-11 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 3ff9daf4-37c4-3728-93f6-0e12d81b4a6a | -8.9598 | -60.555 | 2026-08-11 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 8ebc58da-3cc3-39c0-8790-a1307756b48a | -8.96 | -60.5358 | 2026-08-11 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| bfa4fc3b-e775-3efb-801e-0d57e7e0054e | -8.9416 | -60.4982 | 2026-08-11 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e5343358-3a40-3f38-8aa6-87fc94f41241 | -13.5502 | -46.2844 | 2026-08-11 08:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 22790d36-c43e-360d-aba4-4f6fbc843560 | -9.3909 | -47.4656 | 2026-08-11 08:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e78914b9-80ad-37c0-9656-cc5bd555ad82 | -8.96 | -60.5358 | 2026-08-11 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| ac716858-a562-3342-b579-7bff7b796839 | -13.5507 | -46.2615 | 2026-08-11 08:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 131e6a77-e860-31db-b7c5-f8680055a4cb | -13.5696 | -46.2813 | 2026-08-11 08:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| de0047ed-1545-3dad-9d56-c18b1ec56185 | -8.9415 | -60.5174 | 2026-08-11 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a34ac4df-8cfb-30d0-bc4b-0b02ca363c31 | -13.5502 | -46.2844 | 2026-08-11 08:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f943fbb6-a289-3832-985a-585580ccd343 | -8.9602 | -60.4973 | 2026-08-11 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6614ce44-d551-3712-b828-8f0941db99d4 | -8.9601 | -60.5165 | 2026-08-11 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f59bb7ed-35a0-3fad-8473-ab87c64f9ce3 | -8.9598 | -60.555 | 2026-08-11 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e6129954-0f48-372f-b20a-8029f66f639c | -8.96 | -60.5358 | 2026-08-11 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 497f3ee4-7f7e-37cc-8a17-7de25a1e05e8 | -9.3909 | -47.4656 | 2026-08-11 08:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4182ad24-594e-3ccf-9037-3062fb7c52ab | -8.9416 | -60.4982 | 2026-08-11 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2c5cf271-f785-300b-933e-afc94f462769 | -13.5502 | -46.2844 | 2026-08-11 08:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 58d45977-3238-356d-9ead-bc48db9a4667 | -8.96 | -60.5358 | 2026-08-11 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 67e52692-693d-3924-8fa1-ef4d48bbaee5 | -8.9598 | -60.555 | 2026-08-11 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 38f9174e-caa4-3a55-bdbc-ed688057f2d9 | -13.5696 | -46.2813 | 2026-08-11 08:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0bcd6607-22f1-37c1-93aa-67d9ff079872 | -8.9415 | -60.5174 | 2026-08-11 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8a3d91de-23ac-373d-be05-eb1cef4a997a | -8.96 | -60.5358 | 2026-08-11 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5804bce5-c176-398c-aa73-def93a6fed9d | -8.9598 | -60.555 | 2026-08-11 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 99601130-8a90-3a44-9958-fdaa2a37b5fa | -8.9416 | -60.4982 | 2026-08-11 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 7be8ad6b-ea4a-35b9-8c92-3042c29fc009 | -8.9414 | -60.5367 | 2026-08-11 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 522a0a0a-7ac0-3294-aa6d-777daec87c99 | -8.9598 | -60.555 | 2026-08-11 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a7aca3e1-cc5b-3aac-8f7f-210fa6c75ede | -8.9416 | -60.4982 | 2026-08-11 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 12465acd-be1b-3cfa-874b-e80dd4ad025d | -8.96 | -60.5358 | 2026-08-11 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b55319b1-1636-36d8-a2b3-28ea13786a16 | -8.9415 | -60.5174 | 2026-08-11 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 84742f16-23c8-3186-862a-7976c97e68ed | -8.9415 | -60.5174 | 2026-08-11 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5980bfff-eb20-3273-9ccd-788dfd23f3b6 | -8.96 | -60.5358 | 2026-08-11 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7a59a251-cda4-3903-8af8-7e0d4a7caa61 | -8.9601 | -60.5165 | 2026-08-11 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 04937985-5c1c-3616-92d5-ea28049fee9a | -8.9598 | -60.555 | 2026-08-11 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a10ef6b0-e24d-3958-8387-b1a9f0644172 | -8.9601 | -60.5165 | 2026-08-11 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| eb60e407-8a24-3050-95de-2477dd6ee0d3 | -8.96 | -60.5358 | 2026-08-11 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 28804807-114d-3c3f-bf03-f978f452453b | -8.9415 | -60.5174 | 2026-08-11 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 08aaddca-0ab6-3ec9-8dac-7921d2b917ba | -8.96 | -60.5358 | 2026-08-11 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7d733a56-5fa9-37fb-8348-e8fa8255e47a | -8.9602 | -60.4973 | 2026-08-11 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| bf227759-a3cf-3793-a9d6-a7ca6ba63434 | -8.9414 | -60.5367 | 2026-08-11 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3b5f56a3-b958-3169-be79-7808ad543af8 | -8.9598 | -60.555 | 2026-08-11 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6b4b0d31-c9b5-3cf1-8abb-c9a18e0ccf87 | -13.5502 | -46.2844 | 2026-08-11 10:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 93c78aba-e7e7-3233-8c19-2c929220811f | -13.5502 | -46.2844 | 2026-08-11 10:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 1fc99e66-da0b-354c-a33f-df230adfb7ce | -13.5502 | -46.2844 | 2026-08-11 10:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 9ec0065b-5f8e-3f41-b454-e9d1ec4fe0b4 | -13.5502 | -46.2844 | 2026-08-11 10:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ca5acd5f-4a7d-3026-ac80-3597fb455297 | -10.4237 | -46.6809 | 2026-08-11 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 81903f99-90b4-37e8-ae89-fcaae6b374e7 | -13.5696 | -46.2813 | 2026-08-11 11:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 75e713a4-aa14-3e8b-b3c4-b1873a3326e0 | -13.5498 | -46.3074 | 2026-08-11 11:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 321a494b-9b41-37e0-a533-84a2aae74659 | -10.4237 | -46.6809 | 2026-08-11 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| edbc6d52-7dc2-3a53-96a6-6cf819177f80 | -13.5696 | -46.2813 | 2026-08-11 11:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8120ad6d-50da-3955-8d92-1eed1436ab4b | -13.5498 | -46.3074 | 2026-08-11 11:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 19264afa-b9cf-3eec-b966-5100d2de718e | -14.2877 | -45.2835 | 2026-08-11 11:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 859e33e9-3e0f-3854-9549-5e37e6392ebc | -10.4237 | -46.6809 | 2026-08-11 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| fe029f82-4bdc-3c15-a178-b76ec74becfa | -13.5696 | -46.2813 | 2026-08-11 11:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0dc909cf-7fc3-3b67-b970-ed225e0025ec | -14.2877 | -45.2835 | 2026-08-11 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 6c80bc12-f5d3-3c0e-b527-f797f7be6aaa | -14.2877 | -45.2835 | 2026-08-11 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| bf58b32e-7103-3820-97e3-3416245e0804 | -14.2877 | -45.2835 | 2026-08-11 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7002d134-1135-3824-9f22-80f725c7a4ea | -11.6601 | -51.6644 | 2026-08-11 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c81cbae5-b97a-3595-87eb-610e18347eba | -10.1084 | -46.2018 | 2026-08-11 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |


[Clique aqui para ver as próximas entradas](README32.md)
