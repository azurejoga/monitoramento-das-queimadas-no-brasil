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
| 0fc4d726-f8f8-3a7d-b480-321085ee38d6 | -2.27141 | -51.24046 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5cd11df-e4cf-3d2c-aaab-46ae43faf5c0 | -1.27664 | -52.70152 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 825dc396-5e0a-32cd-836e-9bbd89000cf9 | -2.4637 | -53.96807 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d09d18b6-4af2-3882-b204-52542b6f7785 | -2.43709 | -53.89644 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 501f4199-08c3-3b2f-bf78-68bdee2c806a | -2.76545 | -54.06135 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7519068b-e64f-3b8f-b588-8cf3ab35550b | -2.30309 | -51.26474 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 092f4cd7-eb4a-3360-ae00-11e51bb93f61 | -3.05742 | -54.41162 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb60b3a1-d8b3-39c2-8529-04cf555adfe6 | -1.99004 | -54.90123 | 2024-11-29 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be6a54ab-454e-3965-87a1-4aea9892a8a6 | -2.29093 | -50.68958 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3543c30-27f6-3a74-988c-cfaf41b0ac68 | -2.76929 | -54.05842 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba6b1a00-1469-36c4-bd55-54670868e45f | -1.32237 | -51.75119 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d55b40c-e861-3217-8214-55a63cb2a168 | -3.24971 | -53.63715 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0ddd6f74-c445-3fc8-b5b0-5d4281bcf014 | -1.70603 | -52.76157 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c7395fc-ef46-3188-9f7d-fea16fd8e0d1 | -2.8206 | -54.07691 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dee550ff-8485-3a2f-8a3f-fa25cafd9405 | -4.43575 | -46.58266 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 740ea22f-cf90-300f-b0b4-740cd00fd9f0 | -3.09855 | -53.25412 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0157f8e-85dd-3500-83ac-5e8d352c7433 | -1.52982 | -52.6914 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5db8a6f2-c0ae-327b-aa80-38123f119d45 | -1.58129 | -53.84366 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 3c9a2cd0-c7da-3acd-a3de-640a3f350f17 | -1.30771 | -51.73418 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b36ae98-a1ff-30f3-be30-72cbb15ee17e | -2.89705 | -51.36774 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 741c9783-9b18-3c8f-951e-d1a064a2f73a | -1.06266 | -51.75537 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa4b9b75-9d2d-3624-9406-608c3add70d8 | -4.9314 | -44.52522 | 2024-11-29 04:57:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc29c0cb-12fb-3bf6-bfd9-13e9cd6ca045 | -1.20534 | -51.7814 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18221913-5a0b-3080-a099-5bff5fa5fd45 | -0.91851 | -51.63822 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a122658d-f5a3-36be-8dca-912198053daf | -2.59003 | -54.07237 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 373fcdac-4609-3233-b382-6c7d68aa3d77 | -1.13976 | -53.62254 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faf47834-ed94-3438-ae7a-cc6099ff6977 | -2.5963 | -53.96746 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a125d11f-997d-3e60-873b-aab34f43e7eb | -1.12534 | -53.73652 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ed1b64b-27d9-3928-81d6-fafc8e36e1e8 | -1.29475 | -51.7285 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b4dd37e-9037-31d4-8284-09879cb0329d | -2.98562 | -53.89112 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b1a032d-d8fd-38b6-a3d8-f308946aa4f0 | -3.05052 | -54.04204 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6675004-2e94-3399-860c-840d06b6fbf1 | -2.53613 | -47.32917 | 2024-11-29 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9fbb0a3-be0b-361a-b2ca-5ceeb72a4ea1 | -5.75071 | -43.39948 | 2024-11-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| becc5124-842b-3ef3-8658-c5223d51d30e | -3.38999 | -50.31964 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 239ae18a-ad1f-329d-b6f4-51995662c9ed | -3.11542 | -53.75651 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24d7358a-000e-3cf6-a101-be7099ebfac9 | -1.3972 | -52.561 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2537df1-f2d6-3dd5-89f0-880c07e88691 | -1.17628 | -53.41034 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d098c58-a814-356d-87db-c54fa0bafe70 | 1.22943 | -55.93809 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a826ae2a-c2be-39ce-a954-551ff10354c9 | -2.95633 | -51.2829 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 317a5863-5d7a-33ac-86aa-512dc1ef87e4 | -0.24368 | -53.76199 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15809cad-a19b-35d6-9122-1529dbb4542b | -2.73717 | -52.58287 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8be578e5-6f3c-3ce5-a39c-763b0dd899ec | -3.99766 | -47.91399 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40e34e89-a05a-3f9f-ae4c-b6d4dcc7a68e | -2.90144 | -53.05696 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 072b7040-3230-310a-9f9d-7fe24420f682 | -3.36974 | -50.17932 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 245fe337-2255-3521-a9ea-948a0d0ffb09 | -2.9682 | -53.93771 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68902715-10ce-3d52-af12-7333f0433518 | -2.41618 | -53.90027 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22c4f2cc-eba4-3c99-953d-e625bf4be35f | -3.2229 | -53.4184 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fced4343-bf1f-37eb-b8fe-9ace2afad1c8 | -2.72403 | -54.10716 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79924ce5-9042-3ce2-94c6-2b742bc050e5 | -1.74928 | -52.65833 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ffdc7f9-48d5-360d-ba5c-77147ee35679 | -1.08819 | -53.38615 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8b83a1a-303f-35f7-8c26-bee6ed08d1c8 | -2.93329 | -51.77124 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87871192-b9f2-3805-a0ea-a70a4e1f2b50 | -3.77181 | -46.68272 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfe2718b-1cd2-35f4-86ac-4ac8db61505e | -5.28363 | -45.12597 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3714aa91-1546-3588-9b0d-77354bda57a7 | -2.83083 | -54.01151 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2186edb9-32e2-3580-ac1d-0352dc0ad185 | -3.65559 | -54.17602 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb5348ea-0c86-3230-aa72-10866f322e71 | -1.65953 | -52.25069 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76be5e28-ecbf-3453-af6d-27d8bc1dbac2 | -2.31756 | -50.65598 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e80b67c9-9ef7-3329-b745-ef9040c29ca6 | -1.51981 | -54.41043 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e45ae99-b6b4-39dc-87bd-c689c60ccecb | -3.26193 | -53.27636 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92922325-6fcb-323d-8e33-505576a205ea | -3.78628 | -50.34647 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f834d183-e53f-3b6a-888b-f3d5fd86069a | -3.08218 | -53.29393 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4adc101a-661f-31dc-9a1d-625d5164d908 | -3.74014 | -51.83898 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34ff9eca-52ab-3a87-ba07-bfadb0ae09e3 | -2.80704 | -54.14193 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d616f1b6-96e8-3e09-94d8-97c7985a20b3 | -2.69503 | -51.99665 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5e7f43b7-969d-3ebd-91d2-7b4bd23fce64 | -2.84306 | -54.04158 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf1dab3b-7744-3f9d-8bd8-cb798a456c58 | -3.25982 | -54.11746 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aabf2ce-54c6-3784-b55e-1b4792513244 | -3.28643 | -54.16391 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4549770a-769a-3aeb-86da-749490d210a3 | -1.89653 | -54.54833 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f03a455-2b97-397d-8d34-0aac87dd946f | -2.82161 | -54.04885 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a46306a-8073-3335-b760-07ba661cba67 | -1.1919 | -53.8991 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 541792fd-d097-341d-9950-2ba6c692f6ff | -2.01358 | -46.39729 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0db327fb-a484-30a9-ba64-849196f7ae6b | -2.23786 | -53.62637 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 382e6bb9-520a-30af-8c30-8b292f91c31f | -1.60229 | -55.42086 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbb0ed01-ec99-3483-be9e-bcbb9d049e75 | -3.27413 | -53.83099 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88bc0adf-bf08-3d81-bc7d-601bf1eae053 | -2.83399 | -54.12135 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5321cf9-c434-3c45-9ad6-7638f3bc6371 | -2.44843 | -53.97571 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ee4c34d-6c91-3093-ac83-136204e18f9e | -3.10696 | -53.98794 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 937df567-fa3d-3752-a935-6f4f9b657720 | -2.83284 | -54.10704 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9c3c752-9de0-38ca-9b85-a0a0f23f0082 | -3.21906 | -53.42133 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11e7f834-f35c-3a96-94b0-5a3e2c1a8efb | -2.80291 | -54.06007 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d97633b-643c-3119-8eae-3f4065df4374 | 2.0927 | -50.64565 | 2024-11-29 04:57:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fc613dc-5f5d-3ae0-8213-a371db9d211f | -1.18464 | -53.8804 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b1abc67-f982-3de6-abb7-982e32b5f054 | -2.77375 | -54.07322 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38b22929-2c16-3f35-9917-524a3920e0fc | -1.1261 | -51.68049 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31eae3a4-b52e-3a3a-aef7-f8b7d7578c3e | -3.41278 | -50.24384 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a87ba6e-3023-30a5-84dd-9ac33f046448 | -2.95074 | -45.72006 | 2024-11-29 04:57:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 44474edf-c8c6-3a1b-8dd4-bc05f436cd87 | -1.16915 | -53.67279 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b311698-7803-3891-aab8-f9e2766eee84 | -0.98541 | -53.67602 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14ace6a6-f961-3913-b154-6ca4fba7503c | -3.72463 | -51.09483 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b208d7b2-79d7-3231-8377-4fb0a6740347 | -2.272 | -51.23666 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cec45d3-2b8b-3016-852b-a251928e5b9d | -1.97659 | -52.0748 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c81ce443-dbe4-3dd0-8f7b-fcbb72df82d6 | -1.71663 | -53.06308 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b20d012b-7c7b-3521-85d5-8e046584abaf | -1.07 | -53.63282 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5b0278f-1875-3018-b5cc-3e4920c0d319 | -3.39627 | -50.30301 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a1a8322-72c8-38a6-9425-183ae8cc4fab | -2.61043 | -54.07198 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 686fa241-e5db-34ff-90d5-591b2820e406 | -2.8698 | -53.97874 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed8445e6-b2ab-328d-b5ef-6f9acd167b5c | -3.89828 | -50.19605 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1477d657-e188-3286-a18d-37862dece96c | -2.89725 | -53.95846 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0706c480-4910-34d6-ab90-0d7e867b6aee | -1.62559 | -52.53558 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28ee51d6-8dcd-30f3-b716-cd516163bf44 | -2.58367 | -49.22361 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README71.md)
