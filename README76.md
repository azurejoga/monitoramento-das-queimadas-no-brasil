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
| a9c80e6d-b86b-3237-9671-aa3d47c59a66 | -3.48461 | -53.80626 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 189ce2a4-7cd3-3893-919d-57d76c298510 | -3.73239 | -52.33814 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c0e5982-9ea4-3a1b-8ac2-e4b99a687840 | -3.86492 | -50.15405 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1d15369-fe71-38dd-8661-7fa06e735791 | -3.52972 | -49.90335 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f051936-bc59-307a-a808-110830505ddb | -1.45545 | -55.18398 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1970dd6-6860-3127-9985-b39ab2366fd8 | -3.49808 | -53.80839 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2ab11ef-a626-33f7-a9f2-607ae1397a03 | -3.67418 | -52.11094 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6da05bf-3d44-3d17-a62b-235a757741fc | -2.62083 | -54.20903 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8446e25c-d78f-31ab-b02b-1bfd1e54326a | -2.83824 | -54.05031 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfc8723c-aff0-3522-914d-b8ba22f56f09 | -1.22026 | -51.73625 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c214dff-0b58-3b49-8ebb-9b0a49c4d71c | -3.16458 | -53.23615 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f26fab31-0258-3a29-8d87-4f4002f66e81 | -1.10644 | -53.40486 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c313d16-9a1a-3d4e-9572-e1199158704a | -1.62651 | -53.88031 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 438da4dd-913b-3014-bc05-15ea97aa5b12 | -3.14259 | -53.83051 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ef47ed5-8e9b-3760-9998-46f4a868d13e | -2.866 | -54.00437 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38268e95-2dba-30ec-a370-8c7910c80ce4 | -3.24894 | -50.58248 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20e48baa-7366-3138-8c98-120d3d2b38fc | -3.25851 | -53.64068 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0ebf85ef-d2b0-3784-b8a0-c90a464c1091 | -1.65012 | -52.40611 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f86ac73-c2f8-3a16-88fc-cd09ab5370b1 | -3.69526 | -51.36836 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2092ac66-df67-3717-9994-a9eaeba631fd | -3.4684 | -54.54022 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20b51d69-73aa-3114-a4f9-54d238870ef0 | -1.24272 | -53.35674 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7eac3579-660b-36de-a905-5ddb04363bf3 | -3.31173 | -54.09123 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d147523-c9d3-3599-a848-c065774e3f8c | -3.59753 | -49.97965 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 361a5ea0-79d7-32a7-84d1-6a39c528783c | -1.94792 | -53.34082 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 56f3dae2-f9b6-3f78-88d6-c733da74dc16 | -3.07769 | -51.09734 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8597f1ab-ff8e-3bdf-9470-b5e394078d82 | -4.59226 | -44.70814 | 2024-11-30 05:01:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fd89ee6-7e77-35d1-8a94-a6cd9e13b1de | -1.12652 | -53.18943 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 715d8da0-3474-3c46-aff2-69409fda0809 | -2.62137 | -54.20555 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4abe2c2d-8841-3d01-af66-c2e99939b383 | 1.90066 | -55.82509 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2557891f-7131-378a-a594-62df137637d5 | -2.32418 | -50.67826 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35beb802-88d1-31c4-ab5b-2f6e20ea2010 | -3.57682 | -50.33624 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c10c5078-6678-3a9b-acdb-ceea4b9fb1d4 | -3.70369 | -47.13565 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9aa2139b-9649-3440-b585-6f6481d0b9b0 | -1.32153 | -51.66384 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4f4f9af-2808-3ae2-983f-b24f4ee3c399 | -3.31295 | -50.02461 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ce61cb7-e48f-33dc-9bd8-5c8c1b5f8542 | -1.33284 | -55.85103 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 77c902cf-d98b-369b-8a1f-16bd47735dfc | -3.08346 | -49.20621 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0686c27a-dbfa-36b2-93a8-effde477c4b8 | -3.03065 | -54.05109 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d122947-ceeb-3890-8301-91d967b3d386 | -1.79364 | -52.73881 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 919b29fc-cded-3ee1-abb4-b90014008da6 | -1.25446 | -51.63401 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d2d42e4-87fa-3b44-8fd2-13e60ed6777b | -2.80289 | -53.11783 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 301e5785-03ea-3bae-bed8-7a61df62d2a3 | -2.574 | -54.33332 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad38f4b5-0e3a-3958-98b3-2681d8ede127 | -1.7194 | -52.63237 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6994af31-ab57-376b-8865-044c200b00b1 | -4.12431 | -48.84595 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f71a840-7b86-3818-acaf-3f2bb0a45396 | -4.68326 | -42.36979 | 2024-11-30 05:01:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2900e69b-01de-3e1d-be6c-a29506aba0dc | -1.24781 | -54.54729 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2e304b7-9fc7-3cc7-8c29-1b47f9895809 | -1.50974 | -52.56681 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b4372533-d5d7-3c68-aa37-f87ef87fa8ee | -1.0818 | -53.38652 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be1173ea-9ff2-3aff-95dc-39162cc3ee63 | -3.09657 | -54.12635 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f57411c-f4d1-39b4-b8cd-64095eed497e | -3.08983 | -53.24769 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2661439-7c8a-3f9d-bcc0-74f91cbb7855 | -0.05237 | -50.83146 | 2024-11-30 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d03ffb89-4812-315a-b722-34873f0d9a9e | -3.27089 | -54.70119 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46ae5691-43c0-3cb0-9065-25f23f7cb514 | -2.77456 | -54.02985 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4eacb6e-e74b-3a51-974c-d6602afa4392 | -4.87109 | -41.29465 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1ed31f57-c447-3b30-852d-41d3055de636 | -2.8566 | -54.0424 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c64aee5c-7371-36fa-b533-e13a46934f11 | -1.9213 | -52.88357 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2f0e116-1346-35b0-8e13-fdf373952fcc | -2.27415 | -46.43632 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08b6b511-9c26-33e3-971e-999801d4ca17 | -3.25625 | -53.63299 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 71de50a0-de6a-3850-8abf-94b11bdd68b2 | -1.26717 | -54.55383 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 392d98b1-4ff3-3889-b7f5-79a6476eeda5 | -3.60404 | -49.99147 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5db448ae-859e-3a01-86e7-7bb3d8f7cafd | -3.40506 | -50.6599 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2bda2c67-5224-3730-9a90-6cb69a8d9f2a | -4.18775 | -54.76267 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d30d2e8-8a9a-367b-b42a-5c3241b754f7 | -2.59996 | -54.08089 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf66c014-0f68-3c4b-9178-00e3dd1ff937 | -1.13211 | -53.71082 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 205732ba-2e9f-3879-958a-ab2357f35dcf | -1.09803 | -53.39268 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5671f46e-0e41-3baa-bd24-24d660ada05a | -2.225 | -53.68856 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d123970-4525-3298-9b01-b2d388003d9f | -2.83069 | -49.84231 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7688def4-ea49-3355-aff7-82258ecd5e8b | -1.3952 | -55.00795 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6d29045-80d0-343e-8ae4-dc6263a6b46c | -0.95575 | -51.65758 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7e6d77e-d38c-38ef-aeeb-de673e3bdd53 | -2.81934 | -54.06173 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63f1fb01-944d-3ba0-b154-3b6eefd65410 | -0.96533 | -51.71243 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb2e952a-cc87-3cf5-9b82-8dcec5677cae | -2.88217 | -54.01048 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89fc621b-fa64-3655-9731-ec860975dc4e | -3.58084 | -52.29698 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f7037d-6773-3b24-8585-eea8b4745338 | -3.23699 | -50.24538 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20af763c-06b4-39f0-8692-5305c8bfbd3c | -1.68325 | -45.79002 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37e000e2-2924-3a12-895f-6957ff26e464 | -2.57864 | -55.99397 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba444bb0-8ab4-36fe-aea1-529806e259c6 | 0.93602 | -50.74212 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6ab4b292-1701-3b9a-b9ee-8502a7a3e3e0 | -1.79421 | -52.75791 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d365c922-60a2-3b6f-88c3-eab65d5571c1 | -2.69233 | -56.90022 | 2024-11-30 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b98bad34-b0bb-34e7-8a8d-dfbd9ac86120 | -2.74196 | -54.15001 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 045f2aef-524a-3ae7-bbcc-12e073b7db15 | -4.05147 | -54.44599 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6011e6f6-f4f1-3298-a71b-de62baad2c7f | -3.73533 | -51.83489 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce68fb0-0022-3234-9f71-d37bb8e2ec88 | -2.61804 | -54.20503 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b89496d0-8d55-371e-ae02-e0f3f5070a81 | -1.68557 | -46.78439 | 2024-11-30 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2226b28b-ef19-3833-92b2-b5278d4749fe | -1.42545 | -54.94545 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd7237a4-d472-3cf1-93ef-6a8c4365c1cd | -2.23507 | -53.69013 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 423fcc40-1e43-30cb-a55e-414865dee43c | -1.09579 | -53.38506 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed6066af-2e4a-35b3-b658-4b3b4025ead9 | 0.97189 | -50.12589 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25824ba5-189c-3fcf-a9c4-f34da13f909b | -3.8164 | -50.95216 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b774cbf-7acd-3f79-86ab-c47e810968db | -2.77177 | -54.02582 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ce9d397-33d5-3ea9-bdc7-0d4070846b06 | -2.65486 | -51.71442 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da82425c-eb7b-337d-8c3e-9045ddbd22d4 | -1.85449 | -55.61748 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 347e4057-a37e-3b8f-ba39-67fa2483b78e | -3.11681 | -53.2738 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5120415c-0780-379a-9b37-f3c93f78d650 | -2.36393 | -50.5194 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 74675b7a-69d0-3722-b767-df909124865c | -2.32942 | -50.66946 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa15c2db-ca75-3b17-9c2a-7680ed8c4c50 | -3.12796 | -46.05153 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16b338d2-9747-3cdf-a3e8-b22df76d952b | -3.4908 | -53.81088 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2e05cc3d-82ea-351f-a08a-086a3d63f2e0 | -2.98604 | -53.28444 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91637181-ba5e-3e6c-a7e8-88609ede6d0f | -4.0666 | -46.68401 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3db6d230-261c-340c-986e-8e9d449231d1 | -2.73798 | -54.11009 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b35ee91-ef66-33e5-8118-9046de598117 | -2.82317 | -54.03722 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README77.md)
