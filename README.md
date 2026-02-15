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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74b0fadf-e8de-3d98-b8a2-0056a6c594b6 | -15.8365 | -42.6633 | 2026-02-15 00:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| d182a2c1-943b-3a19-83d8-2f0e81f77a0b | -15.8359 | -42.6879 | 2026-02-15 00:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.4 |
| a7c38fd0-a1e8-3c30-9d09-9d780b0d002c | -15.00417 | -45.15331 | 2026-02-15 00:43:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 415c123f-8144-3581-a851-3ed033f98fb9 | -22.04782 | -51.45995 | 2026-02-15 00:43:00 | TERRA_M-M | ÁLVARES MACHADO | SÃO PAULO | Brasil | 3501301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3315713b-20aa-386a-a3eb-4a12c990fcca | -15.00622 | -45.15963 | 2026-02-15 00:45:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5dfb14c1-ab1a-32b7-a128-7f04c02ea10a | -10.98754 | -53.98693 | 2026-02-15 00:47:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1ff2d356-c0a8-3a55-932a-dc3277fad81f | 1.91487 | -60.58511 | 2026-02-15 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e135557a-e303-3f79-b1f8-56c7e34e4f5c | 4.40749 | -60.05296 | 2026-02-15 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b1e58843-192a-37b0-9a65-226c801678cd | 1.91648 | -60.57393 | 2026-02-15 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 55d61c1e-3701-3f35-b7e5-46ef9a1acfe4 | 3.81604 | -60.89366 | 2026-02-15 00:49:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4f0c35d-e838-3f46-970a-acebfadb1aaf | 3.82436 | -60.90546 | 2026-02-15 00:49:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9e809d43-3266-34d2-9e47-45de005682f2 | 1.91586 | -60.56796 | 2026-02-15 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ee3b5458-348e-305d-aecc-e16e3d67abbb | 1.91432 | -60.57916 | 2026-02-15 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 81dc52cc-9959-3ce9-a7c1-cd61963808e5 | 3.40872 | -60.65941 | 2026-02-15 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 42a54fa8-f121-3b59-a6ff-a765a6c1deaf | -9.92049 | -37.09257 | 2026-02-15 03:12:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 662541f8-bd9c-32b2-91d6-0a4bb4ce48a3 | -11.82558 | -38.25393 | 2026-02-15 03:14:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 593b94ff-b783-39ad-a9b6-4ec892a53f59 | -11.82626 | -38.25045 | 2026-02-15 03:14:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b6d0591-808a-355f-817b-d32916971d14 | -18.7142 | -43.0125 | 2026-02-15 03:17:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b93cafbb-cda0-3aaf-8940-8b92c1af03b8 | -18.70868 | -43.01566 | 2026-02-15 03:17:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cca57c2-1155-35a9-89d4-4846d3b173c0 | -18.71004 | -43.00984 | 2026-02-15 03:17:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 85d4a64c-1430-33f3-8067-edee50eb2b33 | -18.71751 | -43.00647 | 2026-02-15 03:17:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 502dca45-c030-3a6d-a734-9abb32232040 | -18.7154 | -43.00718 | 2026-02-15 03:17:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0f72dad3-4994-34ad-abda-ddc17a91c46c | -18.71626 | -43.01183 | 2026-02-15 03:17:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e53d4ed1-9d41-3f27-9bf2-59a4ebdec643 | -10.5937 | -44.331 | 2026-02-15 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 380e66ec-967a-37bd-9bec-680e0843d8eb | -10.5937 | -44.331 | 2026-02-15 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 19945920-8078-3253-8098-fc0c9ccf82a8 | -10.5937 | -44.331 | 2026-02-15 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1c2629fe-4568-3af1-8d2b-c358dd7fef9b | -9.91814 | -37.09324 | 2026-02-15 03:42:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 46e13ee2-2f9e-3990-8f29-553151acde1c | -14.99975 | -45.15195 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a38078a9-52cb-30e1-9053-3e7b08293ac3 | -15.00044 | -45.14848 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fe696d4-1d1e-34c1-b737-6b26bfdfc7ee | -15.00112 | -45.14502 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2262d513-5082-311f-bf0e-80c353266b30 | -10.60155 | -44.34145 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 98ffd4e3-6fa9-3561-aa30-38281b7cf26c | -10.59129 | -44.33559 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 66e4c21e-47dc-3fcd-8c88-061ad4872763 | -10.59677 | -44.33666 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9efdafb2-310d-3625-8fb6-3e007fcef139 | -15.00749 | -45.15497 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8dc7445-af5d-31e3-89a1-e958a7827d94 | -14.99363 | -45.14129 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39817686-3df3-347b-8843-0c3c843bb6cf | -17.30185 | -41.63442 | 2026-02-15 03:44:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f2353918-6868-39b4-b44b-d5bff0e83f13 | -14.99579 | -45.1439 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d3513f0-39da-3f67-b44d-d62a00b9457c | -10.59608 | -44.34037 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a7c45eee-2939-3343-8fd4-85d0605addc0 | -14.99896 | -45.14239 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 685f21fa-fef2-3dbc-a791-dc60281fd088 | -14.99683 | -45.15276 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1e99c26-f655-3c5e-a010-feb082eeeb61 | -14.99907 | -45.15541 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f589b94-164a-35df-92bd-5072a6f052ce | -15.00372 | -45.15998 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f005a39d-b3f8-3a4e-b459-a545de6f9b6d | -15.00576 | -45.14962 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3dbe168-1157-3850-9fec-20df95f2685e | -10.59746 | -44.33301 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d413c50b-71a9-36c0-b682-022b31934ec4 | -15.0044 | -45.15652 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca803fec-b460-38dd-a443-7aa0e7850d4c | -15.00146 | -45.15729 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8441f12a-1ec6-3642-a23b-1edd02e0b423 | -15.38428 | -40.84898 | 2026-02-15 03:44:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4b95ea5b-2c69-3fbc-b00a-f40545087604 | -15.00287 | -45.1504 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6ff3964-2139-3e98-a872-81cb47d7094c | -15.38353 | -40.84902 | 2026-02-15 03:44:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9f25721c-7c29-3cf7-8780-52974da20450 | -10.60841 | -44.33519 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0282c914-6a2c-3fe4-ae0b-10c4c7d60cf0 | -10.60703 | -44.34255 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70abdbe7-eb19-3be8-9879-d9961cddf38e | -15.00508 | -45.15306 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 089a37d7-5e31-3d12-8b68-ca02d45a00b7 | -15.00819 | -45.15153 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 589f4f5e-a173-3e02-8abf-7d4efe622edf | -10.60772 | -44.33886 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab9259d-8ebb-36dc-ac45-ef44b0e5fff5 | -10.60225 | -44.33775 | 2026-02-15 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 72009cc1-8284-30d7-a711-fcdbe8b7feef | -17.30046 | -41.63317 | 2026-02-15 03:44:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a1fa5afa-0788-3817-a0e2-d3553e01dd2a | -14.99648 | -45.14043 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 483ed635-a92c-3ddd-a53c-d7ec47201277 | -15.00216 | -45.15385 | 2026-02-15 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50f9cdd4-4016-3db1-aeb8-9a0cb03d2f84 | -21.13582 | -41.24345 | 2026-02-15 03:46:00 | NPP-375D | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 38d747dc-b3cf-3e49-a915-047b9216d154 | -17.84382 | -40.14225 | 2026-02-15 03:46:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1ced205d-844d-38ff-91e9-feaa04d6ca3c | -18.65281 | -40.90063 | 2026-02-15 03:46:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0261ef3c-ee26-35b2-b501-44160107f43a | -17.97264 | -42.34863 | 2026-02-15 03:46:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ecab7e38-d912-3ff9-8941-44ebec8f4e73 | -17.843 | -40.14684 | 2026-02-15 03:46:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 219a32a1-e392-387a-9436-a39889d40142 | -18.71402 | -43.01124 | 2026-02-15 03:46:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f8faed44-db9b-3bc3-85b8-1fe106a86299 | -18.71485 | -43.00697 | 2026-02-15 03:46:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fe703be3-ac16-3f8f-ac84-133020dd472b | -15.00208 | -45.1468 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd8d89f9-a136-3238-8b42-479d2d9db50f | -15.00712 | -45.15052 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ea2cd56-c179-329d-9a1a-e6fa0d621cd7 | -12.06964 | -45.3493 | 2026-02-15 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43d05229-525a-3a8b-a7db-bf47c3003a04 | -15.00137 | -45.15103 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d04d312-fdd9-3ffc-97f9-46f6448a9018 | -9.86098 | -37.09618 | 2026-02-15 04:04:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b13180b-785d-389e-8a6c-2d2e01fc58f9 | -15.00494 | -45.15167 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d04f53c-f670-3a07-8da2-206daad7edd6 | -15.00355 | -45.14988 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc53f744-cf38-39bd-aa23-bd244b7c2c05 | -14.99708 | -45.1546 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eddee32-12df-3d6c-9e8d-445e6eddc509 | -14.99922 | -45.14194 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b721a29-325c-38c6-a3e9-8b569e8e2573 | -12.28864 | -49.03679 | 2026-02-15 04:04:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8576100a-315b-3a0b-a761-2494e3a5b333 | -15.00996 | -45.15538 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c836ed4-faad-3595-ba29-1c182e2c0c29 | -9.91892 | -37.09068 | 2026-02-15 04:04:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7735bd95-afd5-3fb9-9519-429ae7a4e731 | -15.00351 | -45.1601 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00f62b7e-b541-316a-b54e-964e0c1a71bb | -14.99565 | -45.1413 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 419ebb8f-8a38-3cd7-9e5d-3d7f95720cf4 | -15.00208 | -45.15829 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91da0d26-e081-3570-8983-c67cabfaa293 | -9.85905 | -37.0976 | 2026-02-15 04:04:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b551be9e-e59b-31cf-a1f5-06cfacdb33ba | -10.59612 | -44.33407 | 2026-02-15 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c5d40dd-ceb4-374a-9cab-7891f3cf377d | -15.01069 | -45.15117 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b4efb3d-f584-36a8-83a0-2f94db678402 | -10.5925 | -44.33344 | 2026-02-15 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14388187-53d4-3946-84ab-2bc44ddad4b7 | -13.39722 | -43.676 | 2026-02-15 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5be5564b-97b1-326e-85f6-3143d25352af | -9.91827 | -37.09513 | 2026-02-15 04:04:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bdf115d0-2f02-3b04-802a-bc8963d32237 | -15.00281 | -45.15408 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57928a00-2cc9-374f-9ce8-732e685a8848 | -12.50564 | -48.73703 | 2026-02-15 04:04:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c219706-de55-38e0-8071-0d1d59983d4e | -15.00423 | -45.15589 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ae5735d-e80b-3391-897e-52ee3dadc34d | -15.0078 | -45.15654 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 929f5cdc-40e5-3429-9bd4-edaaf9e33987 | -15.00851 | -45.15232 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fe0baa9-9a67-370c-9bc3-51ab72faf2d5 | -15.00639 | -45.15473 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a86fde0-30af-3e9f-b272-14a5de3de7c1 | -14.34254 | -45.75674 | 2026-02-15 04:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df76d4dd-e625-3dad-ba4e-bc84fb4e6d4b | -15.00065 | -45.15524 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8cf3e1c-e872-37e6-bdd6-86a03ed1fe3c | -11.8239 | -38.25115 | 2026-02-15 04:04:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6d5a27c3-11b6-3d40-b550-0caf49a2c37f | -14.99779 | -45.15038 | 2026-02-15 04:04:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e0eafc5-74ed-3649-bb68-f29ec0a7c10f | -18.71514 | -43.01194 | 2026-02-15 04:06:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 566c19c3-b3a9-367a-8293-c06fca3d5b4e | -18.83969 | -48.26668 | 2026-02-15 04:06:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba35d77c-0efb-3ffe-9287-ec4c3c2350a4 | -18.70852 | -43.01079 | 2026-02-15 04:06:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 48e185bd-c45e-36bb-adcd-16f9dad97845 | -17.84558 | -40.14545 | 2026-02-15 04:06:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
