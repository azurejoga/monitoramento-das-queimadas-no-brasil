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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f8d10da-80a1-3c72-bb5a-8ff67ad2d758 | -12.48 | -57.1863 | 2025-05-20 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 443.2 |
| 5bb79e5c-bcee-3f8b-b38f-35f84ec37ce6 | -12.3327 | -49.9641 | 2025-05-20 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 85355e04-e54a-30a0-98c3-65894ab44659 | -12.3515 | -49.9833 | 2025-05-20 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 9cbf0777-a7f4-3b1a-867d-800be1752201 | -11.8863 | -46.9179 | 2025-05-20 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 454a49e0-978c-306e-bc62-11e78f4f5c20 | -12.461 | -57.1879 | 2025-05-20 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 5392ccac-af7c-3b6b-a875-5814bc42d8c8 | -11.4269 | -44.7243 | 2025-05-20 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 53ca4025-b27b-3dcc-aa59-586a022beeea | -12.3522 | -49.94 | 2025-05-20 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 8d1b2717-f087-33cd-902a-4b40bf53ad7e | -12.3519 | -49.9617 | 2025-05-20 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 250.3 |
| ed3268e5-7d8d-3141-b662-28b529e509d4 | -12.3522 | -49.94 | 2025-05-20 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9dfa191b-5871-3104-ba55-f71b0fb5b62a | -14.0269 | -53.0121 | 2025-05-20 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6f770f32-eca7-3939-850f-c86ceb790c97 | -12.48 | -57.1863 | 2025-05-20 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 498.7 |
| 38356a58-3005-3a2e-bcfc-7c56654fcc58 | -12.461 | -57.1879 | 2025-05-20 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| e3e744c9-c19d-3e1b-a2eb-49e384227bf4 | -11.8859 | -46.9404 | 2025-05-20 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 271.2 |
| d460452b-4509-3ca7-9942-dbba22fd9d04 | -12.3515 | -49.9833 | 2025-05-20 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 371215d9-05c6-3809-8337-d62538c01f47 | -11.8863 | -46.9179 | 2025-05-20 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 339.4 |
| 26018014-cc4c-3b85-8fdc-3eb6fea8467e | -12.3324 | -49.9857 | 2025-05-20 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e50dda4d-d0bb-3d35-9ca2-227e7579b3b9 | -6.204 | -43.3241 | 2025-05-20 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 39f87618-98ca-35fe-83b9-400fc6e8e2cb | -12.4798 | -57.2063 | 2025-05-20 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 766e5baf-3aa5-3fa2-a796-80216f044c7a | -11.4269 | -44.7243 | 2025-05-20 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| d08797c4-4d97-3aba-9b10-ab0c52629817 | -11.6999 | -47.7909 | 2025-05-20 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 35656d93-cd0d-3e19-86a7-2fa53a8d8544 | -12.3327 | -49.9641 | 2025-05-20 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 335.8 |
| e40c3b2a-c4db-30bb-8830-b1c1cc99125a | -11.4461 | -44.7215 | 2025-05-20 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| ff645181-75d5-332e-a955-6c0ac35b50e6 | -11.8863 | -46.9179 | 2025-05-20 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 9ed3a979-6868-3f5e-bc3d-3a15aaba9487 | -11.4461 | -44.7215 | 2025-05-20 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4b5ad6c9-251d-39ab-9db5-1fbd46bb60e7 | -12.461 | -57.1879 | 2025-05-20 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| f983421c-97f1-3abc-8a3c-acb48cf061b5 | -12.4798 | -57.2063 | 2025-05-20 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| b7dc6f79-f57b-3f5b-bf22-434adbde2e50 | -12.3519 | -49.9617 | 2025-05-20 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 381.8 |
| f5c057f6-45ce-3769-a1b2-280c1311be4a | -12.3327 | -49.9641 | 2025-05-20 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 202.1 |
| e6a15b17-1388-3b9b-8afa-7e47875ea919 | -12.3515 | -49.9833 | 2025-05-20 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c6602bae-697a-3e51-9cbc-633ab9636743 | -11.8859 | -46.9404 | 2025-05-20 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 234b14fb-ebdd-38c8-9aea-a591274cdc4a | -6.204 | -43.3241 | 2025-05-20 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 6021be18-2a60-3328-98f1-dc572407c2b5 | -12.3522 | -49.94 | 2025-05-20 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| d31241be-5789-3e68-a9e2-35d936ec4d2f | -11.4269 | -44.7243 | 2025-05-20 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 16d14c36-edcf-3182-9c00-7386b04bdd66 | -12.48 | -57.1863 | 2025-05-20 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 408.3 |
| a4990550-3433-3f4d-a036-3783f76359c3 | -11.4273 | -44.7011 | 2025-05-20 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 4db1dc36-60dc-3a43-81c8-d03f3f7bab44 | -11.905 | -46.9378 | 2025-05-20 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| adfc7c60-3f7a-3b32-85ab-11a74868afe3 | -11.4269 | -44.7243 | 2025-05-20 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 238.0 |
| c44374b9-3076-30b0-a316-324a12224318 | -6.204 | -43.3241 | 2025-05-20 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 5ab962f7-95f8-37d6-a6e1-67beb0cfcc9f | -12.461 | -57.1879 | 2025-05-20 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 0bfceec6-ef83-3a8b-90f6-2db609c68097 | -11.8863 | -46.9179 | 2025-05-20 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 261.7 |
| 215cf091-72d0-38a0-b5b0-9f48b31112bf | -12.3522 | -49.94 | 2025-05-20 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 843251e9-f65a-3f5a-ad65-455a70e8bbd7 | -12.3519 | -49.9617 | 2025-05-20 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 7b6dea50-0608-3b2c-a31b-b158e2c50d68 | -12.3327 | -49.9641 | 2025-05-20 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 215.3 |
| d26dccd7-47fc-3a9e-974b-84673b69adc1 | -12.4798 | -57.2063 | 2025-05-20 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 34a97c03-91cc-3375-a56a-54e41bf37162 | -11.4273 | -44.7011 | 2025-05-20 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5121b911-4c53-3eca-b9f1-5302122adba5 | -11.8859 | -46.9404 | 2025-05-20 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 320.3 |
| a732db3f-fecf-315d-a79c-7294f303f822 | -11.4461 | -44.7215 | 2025-05-20 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| ce0547c0-6a71-379a-9345-da9d2d5303a6 | -14.6805 | -45.1191 | 2025-05-20 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f1cd52f3-ce54-3d78-8722-5c1af2183cb6 | -12.48 | -57.1863 | 2025-05-20 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 486.3 |
| 96fce2a6-d650-37ce-afa3-3b98320fb4b8 | -11.6999 | -47.7909 | 2025-05-20 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 4a65f1f1-8d5c-3307-bd93-c47f59346f00 | -11.8859 | -46.9404 | 2025-05-20 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 5ac6242c-ff46-3ee8-88c5-129c65ba12c9 | -10.4535 | -49.8999 | 2025-05-20 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 0c1bb7f8-0e4e-33a8-9132-1598efa6be89 | -10.6091 | -46.9716 | 2025-05-20 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4b016cf4-1ea5-357d-8449-71893473ece1 | -11.4269 | -44.7243 | 2025-05-20 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 316.1 |
| f0c5a985-eefb-3715-b969-18c2659f4d29 | -12.461 | -57.1879 | 2025-05-20 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 294908d4-5343-3120-a0bf-a12676daf3d9 | -10.4346 | -49.9019 | 2025-05-20 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 51d859f8-3e29-398b-9023-cb96a7371844 | -11.8863 | -46.9179 | 2025-05-20 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 242.0 |
| 7dce2370-d089-353b-926e-5f2d9853c346 | -12.4798 | -57.2063 | 2025-05-20 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 15f7e117-2f4f-3abb-8eba-1813c9843ef8 | -12.48 | -57.1863 | 2025-05-20 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 532.6 |
| 268bbaf5-f912-38b8-8bea-5829c9871196 | -11.4273 | -44.7011 | 2025-05-20 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d7336494-0c91-351c-b6ad-8f9d135863a2 | -12.3519 | -49.9617 | 2025-05-20 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 293.1 |
| a4c29cd4-c1c3-3634-9872-d25aea85081b | -12.3522 | -49.94 | 2025-05-20 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d2041d56-0e26-38fe-acb6-abb205f46393 | -12.3515 | -49.9833 | 2025-05-20 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a76c7b7e-75a4-3ccd-8e1d-a4b0fcd6e8ba | -6.2038 | -43.3475 | 2025-05-20 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 777233c3-4989-3003-ab14-84db84b324fb | -6.204 | -43.3241 | 2025-05-20 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 156.2 |
| ec2eb66f-ff43-3fcf-8812-26cab8c24b8a | -12.2946 | -52.4785 | 2025-05-20 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 39aedeb6-d273-3634-b532-73452ed9473f | -11.4461 | -44.7215 | 2025-05-20 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| e6a51131-586b-30e3-bd3e-9343f0de38de | -12.3327 | -49.9641 | 2025-05-20 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| f8f0d0c8-16ff-3f74-870a-4a229d155b00 | -12.461 | -57.1879 | 2025-05-20 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| a6349200-e938-3115-8183-2fe7a0e19e33 | -11.4273 | -44.7011 | 2025-05-20 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| cecc7515-3f2f-3500-823b-18a19e420df1 | -12.4798 | -57.2063 | 2025-05-20 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 5e84ab38-50f3-35a1-b8ef-ea9bce561bf3 | -10.4346 | -49.9019 | 2025-05-20 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 28745d61-f277-3c53-bdfd-9795849c7319 | -11.4269 | -44.7243 | 2025-05-20 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 345.3 |
| cc091ef7-479f-3bbf-9181-016ba5f441a1 | -12.48 | -57.1863 | 2025-05-20 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 493.1 |
| ad2ac6b1-b6b2-3214-88f4-24b28d05ba78 | -12.2946 | -52.4785 | 2025-05-20 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 569d905b-0c94-3ce7-8366-aa1abaf6420c | -12.3519 | -49.9617 | 2025-05-20 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 272.3 |
| ebc0c012-05b5-36dc-ac2f-ec43ed83e00a | -11.8859 | -46.9404 | 2025-05-20 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 225.1 |
| a72ca1c2-cd55-3d1e-a078-6ab846a90844 | -6.204 | -43.3241 | 2025-05-20 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 8aa10c92-a266-303e-9b11-02a2ed99f027 | -12.3327 | -49.9641 | 2025-05-20 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 80af5cbc-7e8e-3da7-9a43-6e4b5a0eaedf | -11.4461 | -44.7215 | 2025-05-20 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 5f171952-f06c-3d84-aedd-4ad65abd9c10 | -11.8863 | -46.9179 | 2025-05-20 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 180.6 |
| a5b2de96-4448-3ca7-8e99-36bcff3347a9 | -14.6805 | -45.1191 | 2025-05-20 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| cca85db5-c1ce-3e82-b3ca-80668b11e771 | -12.3522 | -49.94 | 2025-05-20 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 396adc1d-e530-3ae5-8d7d-f8fbb0cd85d6 | -11.6808 | -47.7934 | 2025-05-20 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 4f974c31-734c-3fdf-8a04-53bc32afcb06 | -11.4273 | -44.7011 | 2025-05-20 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| d519eff8-66fe-3444-b827-75a8c41da076 | -11.8859 | -46.9404 | 2025-05-20 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 250.7 |
| deee4e43-b2d1-3420-b104-c1010f17ef03 | -12.3519 | -49.9617 | 2025-05-20 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 0d1e8f9e-a949-3b53-b567-760b4a04b082 | -11.8863 | -46.9179 | 2025-05-20 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 194.6 |
| cdef6a23-4758-3cc9-ae11-08e6f854430b | -6.2226 | -43.3459 | 2025-05-20 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2b70d7a3-1e66-3848-bdc3-d3e740fdae44 | -10.27 | -46.8113 | 2025-05-20 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 86fd3aa2-212c-35d0-89bd-a03785c9573f | -6.2228 | -43.3226 | 2025-05-20 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 2927085d-b8e0-3e4f-b0fe-d16373bef958 | -6.204 | -43.3241 | 2025-05-20 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 6be1c1c8-4ceb-3803-8cf3-c5709ccaffee | -9.193 | -45.3342 | 2025-05-20 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d0e0225b-e04e-3d5a-96c9-0a7a44c22915 | -14.6805 | -45.1191 | 2025-05-20 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5cba9428-47e4-38c3-9ce0-2683dd9078cb | -12.2946 | -52.4785 | 2025-05-20 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 822c6047-b998-3016-9816-dfe15c657948 | -11.7988 | -44.2733 | 2025-05-20 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a4cc1db1-4bf8-30b5-b5d8-0855f88399fd | -10.251 | -46.8136 | 2025-05-20 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2a9ad048-1baf-3d05-b44e-bacfe279bda9 | -11.4461 | -44.7215 | 2025-05-20 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| b521312a-d920-397b-b9e4-d7e3b004467b | -12.3327 | -49.9641 | 2025-05-20 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 142f81d1-b8f8-3596-af41-f6240c822eff | -11.4269 | -44.7243 | 2025-05-20 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 312.4 |


[Clique aqui para ver as próximas entradas](README17.md)
