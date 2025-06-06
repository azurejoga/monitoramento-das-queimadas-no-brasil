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
| c705df9f-1f8e-3632-a49c-acd95fa64fa0 | -7.0169 | -44.5954 | 2025-06-06 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2177829e-a37c-35bf-a240-8a123771680f | -10.5004 | -53.651 | 2025-06-06 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 8638fc62-eed1-3009-9e2d-2cbb95f35632 | -7.8929 | -50.368 | 2025-06-06 00:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 81b3d5b9-a8c1-3a43-8a2c-f7eba7a9ac0d | -7.9116 | -50.3666 | 2025-06-06 00:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a7ae543a-c61f-37fa-a2e6-bcde0b3fc5d8 | -10.5004 | -53.651 | 2025-06-06 00:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 49d2ea1e-2db0-3d7c-9089-0e6e384f5d92 | -19.4239 | -54.774 | 2025-06-06 00:10:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e5a7932e-2ad9-3272-9727-84144e1d1ead | -19.4239 | -54.774 | 2025-06-06 00:20:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 61.2 |
| eb61da34-4851-34ba-bcc7-221ff0868a26 | -10.5004 | -53.651 | 2025-06-06 00:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| b49fc577-e198-3fd3-83d5-e0a0aa28aba8 | -7.9116 | -50.3666 | 2025-06-06 00:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 96cab601-3d49-3615-b3d8-3ed2502e0986 | -7.7176 | -44.1611 | 2025-06-06 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| b3091223-50d0-30c0-8b9e-dc2ad32d2415 | -7.0166 | -44.6184 | 2025-06-06 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5a966c2a-8ec5-3a41-8e1b-2c24113bda0e | -9.4964 | -40.3088 | 2025-06-06 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 52.5 |
| 848f4e64-f378-3db5-a75e-1fb17b1446ac | -10.5004 | -53.651 | 2025-06-06 00:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 7f993c13-5676-3876-a88c-952a47b29a89 | -7.0169 | -44.5954 | 2025-06-06 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 56789563-ff96-31ef-82ba-e4e17ea4becf | -9.5156 | -40.3061 | 2025-06-06 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 63960628-c792-3317-9112-10137f17e083 | -7.9116 | -50.3666 | 2025-06-06 00:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 33ebe5e8-394d-3acd-8c01-e13fe50a5c46 | -7.9116 | -50.3666 | 2025-06-06 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4f73af97-5c6f-3201-ae67-60f88fcebe44 | -7.8929 | -50.368 | 2025-06-06 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b41f22e8-1a75-3e36-b896-3d5e3b24e555 | -10.5004 | -53.651 | 2025-06-06 00:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| b277440d-8a21-39db-beb0-6273e760e2bf | -7.7176 | -44.1611 | 2025-06-06 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| acacc374-9401-3515-abd1-6c3e77563788 | -7.0169 | -44.5954 | 2025-06-06 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e1decb31-dc2d-3f0f-a9ca-374182f40064 | -7.7176 | -44.1611 | 2025-06-06 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3621f412-56b3-303f-beb3-5951274f4d15 | -7.9116 | -50.3666 | 2025-06-06 00:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 65c9b455-8819-364c-bc38-3b8dcbd78d0b | -7.8929 | -50.368 | 2025-06-06 00:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| ac23febc-3622-3aca-b65a-dcdd3ba3f01e | -7.0166 | -44.6184 | 2025-06-06 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 551d1655-f950-3d7a-a8de-f55734c9ddd1 | -7.0169 | -44.5954 | 2025-06-06 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 53f680f5-9089-338f-ab7d-767fc509b8af | -7.8929 | -50.368 | 2025-06-06 01:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 76729d01-f647-33b1-a880-441ff864ba6c | -7.7176 | -44.1611 | 2025-06-06 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| f34d0836-d44d-3475-9897-34cb84af89f1 | -7.9116 | -50.3666 | 2025-06-06 01:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f5ac2a2d-3692-3b45-b1e5-239cc7307045 | -10.5004 | -53.651 | 2025-06-06 01:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| cb982f9c-d893-3de8-8690-5f868450d79b | -7.0166 | -44.6184 | 2025-06-06 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 0518956d-5da6-37e8-9daf-04d849b060e9 | -7.0169 | -44.5954 | 2025-06-06 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 66bf2bca-fb2a-36f8-9745-b55b226bac71 | -7.9116 | -50.3666 | 2025-06-06 01:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a583395c-385f-31f7-b55a-f64f5eb21f0f | -7.8929 | -50.368 | 2025-06-06 01:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7cacbfa9-15ba-3dbf-b0f8-45552261f889 | -19.43351 | -54.78484 | 2025-06-06 01:15:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a98ca9c6-2ce8-37c6-a69d-313ffbbd5a00 | -19.44103 | -54.77398 | 2025-06-06 01:15:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fb537c74-df69-3cb5-9a6e-61647dec1ed1 | -19.43217 | -54.77545 | 2025-06-06 01:15:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a61f7ebd-3406-361d-b3c7-f338be6e96cb | -12.66634 | -58.21961 | 2025-06-06 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c9c9866a-04b3-3d17-8b96-5373386b5d8a | -11.54027 | -56.4597 | 2025-06-06 01:17:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a45289cd-a745-3e4f-a249-068250ac159d | -13.51888 | -56.57085 | 2025-06-06 01:17:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| efcdff29-f7d1-328e-9129-6204075ab85e | -11.69031 | -54.55803 | 2025-06-06 01:17:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3de665ba-40b3-3825-8871-222e2d522feb | -10.68472 | -57.59333 | 2025-06-06 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| eda07a9a-0af8-3b30-abd7-e7456fecb839 | -10.94485 | -55.33338 | 2025-06-06 01:17:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 289e8f57-71c1-3cdd-966d-2896dde39c89 | -11.1377 | -53.93771 | 2025-06-06 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 87177a68-19c4-3dce-b7a6-667a3b04f534 | -10.81723 | -56.96104 | 2025-06-06 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 73919cb0-8128-3586-8183-b12320942f18 | -14.04269 | -55.13289 | 2025-06-06 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a5aba7d9-75f9-3077-95c6-b9f53df20796 | -10.6651 | -55.31334 | 2025-06-06 01:17:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b93b1c4a-ac04-3451-b01e-431fa95fb724 | -11.53899 | -56.45066 | 2025-06-06 01:17:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ae092759-66ea-3ed9-b7e2-030c4e1e8f29 | -13.71758 | -57.47878 | 2025-06-06 01:17:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cddff227-5c69-3a1c-b52e-e68b44ae5269 | -11.13943 | -53.94932 | 2025-06-06 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f88ab0b9-a6fc-39af-ad58-92bf2b748656 | -13.88475 | -54.68544 | 2025-06-06 01:17:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cde2926d-0f80-3f64-876b-1d88f28baab4 | -11.53771 | -56.44159 | 2025-06-06 01:17:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c38e597d-6084-3eba-bf4c-52849e1b6cd0 | -10.49033 | -53.65873 | 2025-06-06 01:17:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| e4852e89-c7ed-337b-86fc-6175552e83bd | -14.02459 | -55.13574 | 2025-06-06 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9f22983b-ca64-3d04-91c5-559fad44cd37 | -12.52747 | -58.3517 | 2025-06-06 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0701cca8-9ff5-30aa-af56-698b15b75546 | -12.51941 | -58.35878 | 2025-06-06 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a9ef7694-5323-30b0-b407-24230478e1fc | -10.49223 | -53.67112 | 2025-06-06 01:17:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3d20cb90-de1e-31b2-b04c-76bfd8abb8ed | -10.50251 | -53.66961 | 2025-06-06 01:17:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b24c230e-08e9-3527-a07a-98024de6d1e9 | -11.92382 | -54.82793 | 2025-06-06 01:17:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fdf6f677-a3e5-3346-8029-4ba4427132e5 | -13.52013 | -56.57986 | 2025-06-06 01:17:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e86c58bc-6c10-3644-8c03-b502831cd076 | -11.2984 | -53.98317 | 2025-06-06 01:17:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a297daec-7101-336d-9cdd-2c0a5a8870c1 | -11.53013 | -56.45197 | 2025-06-06 01:17:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8229610a-208c-3765-85b3-8026372c2984 | -11.53141 | -56.46101 | 2025-06-06 01:17:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 45d1c64e-f234-30f2-8e02-c49327d15332 | -12.52872 | -58.36117 | 2025-06-06 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 43585986-e519-3be6-a12b-c3639217ce09 | -12.27231 | -55.07762 | 2025-06-06 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 26b602d3-8d61-3203-ac0f-6cd3c263b9c9 | -10.50061 | -53.65715 | 2025-06-06 01:17:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 50601683-6c9b-3978-add7-291e0417fb2b | -11.30013 | -53.99468 | 2025-06-06 01:17:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c22f555f-3f46-3dcc-8453-4674ae7c9f23 | -13.88327 | -54.6754 | 2025-06-06 01:17:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d5b1998c-47cc-3e68-bad2-ee40fc6ca2ad | -11.92234 | -54.81776 | 2025-06-06 01:17:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 87542d66-1910-3fdb-bd5d-ca53e7fe05f8 | -14.04408 | -55.14244 | 2025-06-06 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0f75d019-c1a2-3d1b-925c-8157cf8918a4 | -14.03365 | -55.13434 | 2025-06-06 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e9540501-1193-3d92-9bfe-19edb483a870 | -13.51762 | -56.56182 | 2025-06-06 01:17:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| fe7632ad-f2dd-382a-af0c-dc373cc740ea | -7.8929 | -50.368 | 2025-06-06 01:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 4d9909da-da4d-3273-b86c-37410b543a85 | -7.0169 | -44.5954 | 2025-06-06 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| cbcb0130-3cdf-3456-8c6d-e610132b2556 | -7.9116 | -50.3666 | 2025-06-06 01:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 78974bb2-0ff2-3bef-af17-d59e8babf257 | -7.90942 | -50.37952 | 2025-06-06 01:20:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 33efa2e8-0ee0-3127-9a9a-a84b47f0e2bf | -7.9056 | -50.35527 | 2025-06-06 01:20:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1a466971-cadb-3129-918a-047b46b84ed0 | -6.57822 | -51.1182 | 2025-06-06 01:20:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| bcda0c05-a99b-3e46-b6f0-f061018cd158 | -6.21523 | -55.65446 | 2025-06-06 01:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b512c2fc-700b-3334-b8c6-398ed27b95d9 | -7.9116 | -50.3666 | 2025-06-06 01:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| baa370fa-7a91-3f5c-8998-060fe9c4f11c | -7.8929 | -50.368 | 2025-06-06 01:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 13799d9e-f410-34c0-9474-21af5f20265d | -12.9628 | -46.7626 | 2025-06-06 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 75137526-890d-3b25-aea3-068226c754ac | -7.9116 | -50.3666 | 2025-06-06 01:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 030dfe3b-7901-319f-9eb0-9e4cd8b73154 | -12.9623 | -46.7853 | 2025-06-06 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 876658fe-7028-3af0-bc93-6687eec7cf1e | -7.8929 | -50.368 | 2025-06-06 01:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 24b96530-f99d-39a1-b5ff-5fe0e6b36ecb | -7.9116 | -50.3666 | 2025-06-06 01:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 548fb908-510c-3f03-b17f-8a8e811574df | -9.5156 | -40.3061 | 2025-06-06 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 69dd7d13-01f4-3d17-bcf9-751375116bbc | -9.5156 | -40.3061 | 2025-06-06 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 83099b9e-97e7-33bd-8134-886e799a81d8 | -7.9116 | -50.3666 | 2025-06-06 02:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3a2f9d04-82cc-321f-959f-d23bec32a5ac | -7.0169 | -44.5954 | 2025-06-06 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c54bf2b2-a967-3585-b065-7cbd50438f6e | -9.5156 | -40.3061 | 2025-06-06 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 3c862380-bb43-321f-b444-5b2e0a101a06 | -7.9116 | -50.3666 | 2025-06-06 02:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2001857c-6a89-3da6-ac08-406ec5c86d9a | -7.8929 | -50.368 | 2025-06-06 02:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 6d88d3ad-2c7a-3b42-9c93-3990bf96d7bc | -7.9116 | -50.3666 | 2025-06-06 02:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 3ddf7642-21f5-37a3-bece-8634ed588459 | -7.9116 | -50.3666 | 2025-06-06 02:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| ae81c0b7-e0ae-3c6c-b2b0-3fa3d61b2315 | -12.9623 | -46.7853 | 2025-06-06 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 5dd9260b-6e23-3428-887a-99479dea07a6 | -7.0169 | -44.5954 | 2025-06-06 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 46e7ad98-bee3-3448-a7ec-e30897d4f5b3 | -12.9628 | -46.7626 | 2025-06-06 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 8c7202b0-cde2-3d66-a85d-b7576ef3a6b8 | -7.0166 | -44.6184 | 2025-06-06 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 853214bf-5d6a-347e-835a-240835c5e779 | -7.0169 | -44.5954 | 2025-06-06 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |


[Clique aqui para ver as próximas entradas](README2.md)
