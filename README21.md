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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bdda9cd-276e-34e8-bfd0-d7b4b46de7e3 | -17.7114 | -46.8031 | 2026-06-30 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 755403e6-7fdb-377d-9498-49c7994e19b7 | -12.4283 | -58.4048 | 2026-06-30 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 70ffa7c9-be52-3a02-8f69-b771093d5d27 | -13.2643 | -56.7947 | 2026-06-30 13:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8c224505-3b2c-3b11-827c-53742a613104 | -8.9985 | -45.7418 | 2026-06-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| ea4de13f-3a7a-3668-90ee-8b01c6eabcce | -8.9989 | -45.7191 | 2026-06-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 13de7eb3-5685-38ef-871e-224ac3de2f3a | -8.9616 | -45.6779 | 2026-06-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| ab4ceba6-956e-32bf-9bf3-7a19db293cd9 | -10.291 | -46.6745 | 2026-06-30 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d9df836d-8f98-38ec-a38e-edcdc06da837 | -17.7114 | -46.8031 | 2026-06-30 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 7e42befa-caa9-333a-88fa-6e68f9a337b0 | -11.9441 | -57.7091 | 2026-06-30 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| df79c893-cee2-3354-864a-32f29db40300 | -8.9616 | -45.6779 | 2026-06-30 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2325c155-38be-3b88-ad6c-d8b4de57b6ab | -8.9619 | -45.6552 | 2026-06-30 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 161.3 |
| b4f31ed4-5b10-380f-9537-0f485df3e2a1 | -13.2643 | -56.7947 | 2026-06-30 13:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 61cced07-74a1-3081-b5c1-7e8438b209d8 | -8.9799 | -45.7212 | 2026-06-30 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0986d897-39ec-3651-94be-38e5e0495fd4 | -8.9989 | -45.7191 | 2026-06-30 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 164.0 |
| a298c594-fc18-380a-8b56-638c36489c80 | -8.943 | -45.6573 | 2026-06-30 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 81fcf628-b72c-33a1-8ffa-7a9fb23d2848 | -12.4283 | -58.4048 | 2026-06-30 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 340.5 |
| e04d561a-6bd9-3486-9d49-b6945c85b7d0 | -15.29 | -57.3823 | 2026-06-30 13:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8d5f6f58-f71b-3197-bdce-08daa8d1e9a3 | -8.9985 | -45.7418 | 2026-06-30 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| fd3ba228-1fc8-3209-b92b-8b0888903064 | -17.712 | -46.7798 | 2026-06-30 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 152.1 |
| a9b17222-3247-36b7-ae6c-8df955ba8568 | -8.9619 | -45.6552 | 2026-06-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 172.9 |
| b643740a-b94e-3d87-9307-755467a5c261 | -12.4283 | -58.4048 | 2026-06-30 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 510.6 |
| a59ca294-52c6-3443-a3b2-13d991bdd1f2 | -8.9985 | -45.7418 | 2026-06-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 8ef6787d-d5e9-304e-8472-d477de69c642 | -8.943 | -45.6573 | 2026-06-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3d595d83-bcfc-3983-b207-40dfb4628300 | -8.9989 | -45.7191 | 2026-06-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 1244825c-ad1d-31ec-bdaf-253e94f0f243 | -8.9616 | -45.6779 | 2026-06-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b85f6333-90c0-3b74-b274-50df63cb7856 | -15.29 | -57.3823 | 2026-06-30 13:50:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 9ffa08f3-c71e-3d65-9215-f57787808709 | -13.2643 | -56.7947 | 2026-06-30 13:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 048742f0-c01c-34f7-9cfd-a5ef65a4a312 | -8.9799 | -45.7212 | 2026-06-30 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1fc96183-6e8b-3b70-8672-c607748c2af4 | -17.712 | -46.7798 | 2026-06-30 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 148.5 |
| bc4a3ed8-2c09-330b-9f40-18e60e28a637 | -11.9441 | -57.7091 | 2026-06-30 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| c9a4e906-ccf4-3248-b49a-26387e4c85ba | -11.9097 | -57.3935 | 2026-06-30 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 23a590c5-2c48-309d-b535-8259a2e60303 | -17.712 | -46.7798 | 2026-06-30 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 51672823-5b67-36b4-8729-d640a41b1ec3 | -11.9441 | -57.7091 | 2026-06-30 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c5bec2c3-1dc1-393b-b37e-297d58ec255c | -12.4283 | -58.4048 | 2026-06-30 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 483.5 |
| b9309b9d-a7de-3f05-8d6e-8c93c3caddbe | -13.264 | -56.8149 | 2026-06-30 14:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| bc589d11-9072-3fc3-b7bd-97eed3e8a6c8 | -8.9989 | -45.7191 | 2026-06-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 4a2bc526-e88d-3327-8c0a-b4195a063408 | -13.2643 | -56.7947 | 2026-06-30 14:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 246.7 |
| ef9c9448-35b4-3254-aaea-9195a8a44d1a | -8.9985 | -45.7418 | 2026-06-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| e531a8e2-dd39-3323-ab09-bb8afd5b1889 | -15.29 | -57.3823 | 2026-06-30 14:00:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 96ae8f95-9e59-398d-a7eb-22ce4d6830da | -11.91 | -57.3735 | 2026-06-30 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d8ba6f5b-bbbb-3972-a31b-05115587478f | -8.9619 | -45.6552 | 2026-06-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.3 |
| a891665b-7fb5-351b-98e2-059501e6b928 | -8.9799 | -45.7212 | 2026-06-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9d515e4b-4ade-32e5-b983-ae9c8bcb73aa | -12.4281 | -58.4246 | 2026-06-30 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| b956c908-2c87-3898-8e7d-bd81c4e21b7f | -8.9616 | -45.6779 | 2026-06-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1fc3ec42-110e-3cdf-b8aa-61285bc47537 | -8.943 | -45.6573 | 2026-06-30 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 188770e1-bb6f-33ce-ae13-0eba1d58af06 | -11.9441 | -57.7091 | 2026-06-30 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 58758b96-3d03-3cca-a145-350868d91861 | -8.9619 | -45.6552 | 2026-06-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e9fe0a5b-da40-35bc-990c-abcf90ebb320 | -12.4281 | -58.4246 | 2026-06-30 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 265.5 |
| 5e1e7792-8ff7-3978-873f-edd049733f70 | -8.9985 | -45.7418 | 2026-06-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e696cbf6-b204-3592-8dbb-6d67e9594426 | -11.91 | -57.3735 | 2026-06-30 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b2d027db-ea3a-3590-a4e8-9e8c9335720b | -11.9097 | -57.3935 | 2026-06-30 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 3d2caef2-4220-3c00-be05-d428e035040f | -17.712 | -46.7798 | 2026-06-30 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 8662982c-3dbf-3665-8f3a-ad1c3c26c963 | -8.9616 | -45.6779 | 2026-06-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a49ef602-3f8b-3fd1-8e86-061341cb864c | -8.9799 | -45.7212 | 2026-06-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 1e5e0282-0943-348d-9c8c-e2e72c1fed61 | -13.264 | -56.8149 | 2026-06-30 14:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 42c570ee-128c-3b98-89b5-ba1815b82ce7 | -12.4283 | -58.4048 | 2026-06-30 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 719.2 |
| 7746ed94-d759-38cd-a13f-2b4414f4a394 | -17.7114 | -46.8031 | 2026-06-30 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c3edd46d-87e4-3b53-b898-0a2c93a5733d | -8.9989 | -45.7191 | 2026-06-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| e6cfa71f-9a5f-3d70-93c1-f13c7f26aa84 | -11.891 | -57.3751 | 2026-06-30 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e3964019-aacb-3435-97a1-0809c84d6788 | -13.2643 | -56.7947 | 2026-06-30 14:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 317.1 |
| ac9068f6-1ff8-30b6-b2d9-91e4234d8e24 | -11.891 | -57.3751 | 2026-06-30 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f945202a-27f4-360e-8650-19b0f7a0ada1 | -8.9799 | -45.7212 | 2026-06-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| dc416d68-f96c-3db0-833d-79809b695749 | -17.712 | -46.7798 | 2026-06-30 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 123.2 |
| b260bbf7-e347-339f-995c-ba121af07f12 | -8.9619 | -45.6552 | 2026-06-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 0e211d2f-d668-3b2c-a8be-f4d59ab9510f | -13.2643 | -56.7947 | 2026-06-30 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 283.1 |
| 935ba681-70b7-34b5-a05a-ff9a4e8463ef | -8.9989 | -45.7191 | 2026-06-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 1786b782-5036-3870-aa73-36ea592febb7 | -11.91 | -57.3735 | 2026-06-30 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 190a690a-9ef2-3783-a42c-9e990f4b1b4e | -11.9097 | -57.3935 | 2026-06-30 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 619b07cb-b5cd-31e7-8d53-8be1750c28af | -8.9985 | -45.7418 | 2026-06-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| e0d325d1-981d-34c4-9160-2eb29ecbf2db | -13.264 | -56.8149 | 2026-06-30 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 436e3b59-4d83-38c2-acc5-bd77f2bb8cd8 | -15.29 | -57.3823 | 2026-06-30 14:20:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9cd94704-2d5f-39d2-9744-e6a7b5907690 | -11.9441 | -57.7091 | 2026-06-30 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4841ef94-d1c7-30e6-a8e1-7323c0181b5f | -13.2452 | -56.7965 | 2026-06-30 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 39a34fae-d9f2-3939-aa4f-3afdb212c8b3 | -11.91 | -57.3735 | 2026-06-30 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| bd6d87ba-a568-350e-a6ea-a0d238cadec7 | -17.712 | -46.7798 | 2026-06-30 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 244edb85-b0d8-3099-b0f8-75f46740e9fd | -8.9985 | -45.7418 | 2026-06-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 59d3383d-7910-39dd-bdad-fcdc95e69282 | -8.9619 | -45.6552 | 2026-06-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b1db9fac-19dd-3066-b868-b1c3ebed1214 | -12.222 | -56.5668 | 2026-06-30 14:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c424e8e7-f0a1-3370-ae61-64f541144ae9 | -13.264 | -56.8149 | 2026-06-30 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 2b696ebd-86a2-3ce5-a4a5-cda1ca44a98d | -11.9301 | -43.405 | 2026-06-30 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e3358b5a-f20b-3089-b6ee-70fe24462328 | -11.9305 | -43.3812 | 2026-06-30 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 5cfb08a3-ebf2-38a8-a650-1615c74469b7 | -10.7777 | -54.0983 | 2026-06-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 35723b99-111c-38a2-9f19-e325b719be01 | -11.9097 | -57.3935 | 2026-06-30 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| fb2c6f82-9069-3d13-b7cb-3b0576a07291 | -11.891 | -57.3751 | 2026-06-30 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 90fa0895-3818-3c62-b6dc-5e049f839e93 | -11.9441 | -57.7091 | 2026-06-30 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 65a9fdc7-84e8-3bb4-9351-ff8bf72d13ca | -13.2452 | -56.7965 | 2026-06-30 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 10516c62-479f-3cba-ad25-5e600d2a4401 | -11.6286 | -59.0169 | 2026-06-30 14:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6233d090-93fe-3c90-91a4-55b295472bd2 | -8.9989 | -45.7191 | 2026-06-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 66ec68fe-b4a3-3bdf-9a0f-ce53e8855e6f | -13.2643 | -56.7947 | 2026-06-30 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 541.5 |
| c685dbaf-f8c9-3329-92b4-9a6a1b4d55b9 | -8.9616 | -45.6779 | 2026-06-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d3854064-a611-39c2-95df-63904f032618 | -9.7477 | -49.0248 | 2026-06-30 14:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 551148e4-8e8e-3b42-82e6-c23a6e1fe77d | -8.0928 | -50.9221 | 2026-06-30 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 221d6d5d-6edb-3f8c-b004-9585eed4708f | -17.712 | -46.7798 | 2026-06-30 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 7e326ec7-316e-380e-9bdc-2156e68cebb8 | -8.9985 | -45.7418 | 2026-06-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c58bf069-a8da-3b8a-a479-17cdad86d808 | -11.9441 | -57.7091 | 2026-06-30 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 06ba500e-0f2b-329a-8c77-8c08f3b37985 | -9.079 | -59.4874 | 2026-06-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 5a80c89f-813b-3e5f-a190-5e7476e6b163 | -13.2643 | -56.7947 | 2026-06-30 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 559.7 |
| 5a84676a-1482-3235-835c-56d7d82c6af5 | -11.9097 | -57.3935 | 2026-06-30 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 5d1b32fc-cb7c-32f6-8193-191b11d7e59a | -8.9989 | -45.7191 | 2026-06-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 24d607a0-235e-397d-9fac-4dae7e469780 | -8.9619 | -45.6552 | 2026-06-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |


[Clique aqui para ver as próximas entradas](README22.md)
