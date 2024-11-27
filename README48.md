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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f6b7c8e-5993-3d96-a439-5f18ba3dd51d | -17.70426 | -54.08353 | 2024-11-27 04:23:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a6eac04-06b8-3a9f-8962-80a7af97b180 | -19.76689 | -48.93734 | 2024-11-27 04:23:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ac0c6bb-77da-37f9-a3f4-d3dc96c6df4b | -21.60781 | -57.49975 | 2024-11-27 04:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b9cd251-0dc8-33e3-80b6-309e988689e2 | -23.40695 | -46.55682 | 2024-11-27 04:23:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ce714bf-4f25-3859-aee8-48c9e5c09727 | -18.01653 | -54.00692 | 2024-11-27 04:23:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71b246b9-ba07-3f7a-844e-7bf1222a48d9 | -20.57783 | -44.57343 | 2024-11-27 04:23:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2a9fd6e7-b838-3deb-8674-140d81b7bc26 | -23.4035 | -46.55628 | 2024-11-27 04:23:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a6e8cc2-302b-3732-a9fd-e8991e09f832 | -16.84207 | -46.66735 | 2024-11-27 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7eca3ca-5c57-34d8-91a5-cf63bbb4179b | -21.06227 | -41.81155 | 2024-11-27 04:23:00 | NPP-375D | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 017608a4-346c-37ee-bc11-83596d9aebc4 | -15.2902 | -56.52333 | 2024-11-27 04:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff30a67f-6cb3-399c-b1c6-8f647cd57128 | -16.23297 | -46.50817 | 2024-11-27 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd6127c1-0ebb-3f81-902b-eca72a5cd629 | -22.9817 | -50.40232 | 2024-11-27 04:23:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 36850e89-2491-3d07-b8fe-71e7636bbedc | -20.15423 | -48.9181 | 2024-11-27 04:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4f3a837-17ff-3deb-bf58-118eb895b9c0 | -14.91446 | -52.8692 | 2024-11-27 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38defde1-87c3-3ef9-a033-eb2bc7d5075b | -18.2725 | -47.80096 | 2024-11-27 04:23:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55f1c9ca-2ee8-3f3d-a702-f3ebe7c44e5b | -22.97828 | -50.40167 | 2024-11-27 04:23:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dfcd5ff4-9b21-363a-9128-8e5243dff561 | -20.37098 | -47.11518 | 2024-11-27 04:23:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c13c61b-4047-31f7-b1bd-3104247b8120 | -25.13665 | -52.14342 | 2024-11-27 04:23:00 | NPP-375D | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 73e6c691-6b11-32f3-a505-9d8688256c69 | -20.40587 | -47.17837 | 2024-11-27 04:23:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a9a850c7-619f-3cfc-97ca-ac4430a0f6ce | -17.22861 | -54.44178 | 2024-11-27 04:23:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82cb1aa1-7c2f-3887-9b17-a052b122f5a5 | -17.22957 | -54.43694 | 2024-11-27 04:23:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af5c9451-964b-34b0-ab00-476501181ccf | -15.88857 | -43.46547 | 2024-11-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d0db6295-0ef0-358e-9b22-21788a4cde40 | -12.68303 | -52.26539 | 2024-11-27 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d7330be-cff1-3453-b551-f95026811d82 | -12.68737 | -52.26615 | 2024-11-27 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f6a0abd-541f-30c8-803a-559e12ba235a | -19.17558 | -40.13795 | 2024-11-27 04:23:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 28c5fda8-165c-3bc6-874a-24cb25be4b5b | -23.33733 | -46.77127 | 2024-11-27 04:23:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39f46bce-8820-373c-a89a-0cf54f1801af | -16.67374 | -47.2383 | 2024-11-27 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e57821d-6da0-3e58-91b0-2952074332fa | -19.20693 | -45.37739 | 2024-11-27 04:23:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebf3a5b9-66e6-31ed-b1ca-9e69f8f055ae | -19.20561 | -45.37787 | 2024-11-27 04:23:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c5b1915-0c3e-3364-8a5a-940302612553 | -15.29504 | -56.52524 | 2024-11-27 04:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4984b842-73f0-3716-afde-4c058dbdcd63 | -16.83874 | -46.6668 | 2024-11-27 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fbbb6e2b-f307-3222-aafe-e89dd2fe32d6 | -15.88918 | -43.46114 | 2024-11-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 17631e6b-aca1-3968-9250-d2cd9221cf26 | -23.36215 | -47.05513 | 2024-11-27 04:23:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| afd83739-2d02-3b33-8d77-89862fc00c4c | -20.38679 | -47.47913 | 2024-11-27 04:23:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71fd2186-a83c-3cc8-945a-f765c16c4274 | -14.91525 | -52.86485 | 2024-11-27 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b98cfba6-dc22-3f05-8650-7858664edbfd | -20.38403 | -47.47486 | 2024-11-27 04:23:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ea6d99c-6612-35c9-9cfc-1ef9588cfb65 | -15.29577 | -56.52168 | 2024-11-27 04:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2213ff4-1b9e-3ee2-b2a7-52a5823f3b09 | -15.88554 | -43.46058 | 2024-11-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ef97ba20-df3b-32e3-bde4-c847b7310759 | -20.52112 | -47.33095 | 2024-11-27 04:23:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b91cec63-40cc-3ee1-9e5f-508688ae766d | -17.22406 | -54.44057 | 2024-11-27 04:23:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7375f07-463a-360c-9452-6c16da6c55bd | -23.52 | -46.97518 | 2024-11-27 04:23:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d524904e-4d15-36cb-b656-d598bf2e02fd | -23.68696 | -47.30868 | 2024-11-27 04:23:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6b1a463d-c123-3605-83fc-3b0e6c28d952 | -14.91513 | -52.8674 | 2024-11-27 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17730e24-4ca8-387f-aef4-75f258c7a032 | -23.59432 | -47.4401 | 2024-11-27 04:23:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ad22470-6285-3f71-a8fe-6463e395fe68 | -20.76461 | -46.76799 | 2024-11-27 04:23:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 560d7340-0739-31af-bf21-ea692e72f352 | -23.36273 | -47.05121 | 2024-11-27 04:23:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6ab3fa9a-f896-30a2-bc16-008dc0ac8f2e | -23.63084 | -46.42484 | 2024-11-27 04:23:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b3d1fbee-61e8-3d4f-8ac4-08e4b7269db6 | -17.70337 | -54.0882 | 2024-11-27 04:23:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aa53872-3cf3-32b1-b576-36c4910cd1d0 | -16.37487 | -42.49554 | 2024-11-27 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 428d12e7-140a-31b9-b204-c585f9c2aa65 | -21.60855 | -57.49635 | 2024-11-27 04:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffb202ce-5c87-366e-a0b1-6a19ae1957c8 | -18.01213 | -54.00599 | 2024-11-27 04:23:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5b570593-76a9-3b2c-a8b7-12c8c0e2474a | -17.22637 | -54.43841 | 2024-11-27 04:23:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35b9e427-1650-3493-9bae-3fdebec5ef8e | -16.37539 | -42.49725 | 2024-11-27 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98cf6e72-d2b1-3e07-b03b-c70b036aa5ae | -16.20785 | -45.868 | 2024-11-27 04:23:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ad420f-bcd5-3079-8f49-2523db5b7701 | -15.2903 | -56.52062 | 2024-11-27 04:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 698881f2-9c82-3985-87a6-170430c9f515 | -22.98512 | -50.40297 | 2024-11-27 04:23:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 6a278fea-b95b-3029-bcc9-7c199b91eb58 | -16.67706 | -47.23888 | 2024-11-27 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffe274ec-17bd-3e17-a72a-50e24951795b | -16.70344 | -46.0751 | 2024-11-27 04:23:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46980696-e768-393f-a7ff-f736423f3ae0 | -14.91596 | -52.86306 | 2024-11-27 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6bd5950-8906-335a-bd44-e7dd38ec3598 | -23.36554 | -47.05573 | 2024-11-27 04:23:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 36d1101a-7367-33e8-9117-ac12083d340d | -17.23093 | -54.43961 | 2024-11-27 04:23:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc52f6ff-60a0-393b-a1e7-de02c14438eb | -17.77811 | -42.80992 | 2024-11-27 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a92e397a-8709-3ff2-a70c-64dfaa763b21 | -22.9858 | -50.39898 | 2024-11-27 04:23:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 1c1aa2d1-c5a9-3e9d-a901-7a81b0c687e6 | -22.98238 | -50.39834 | 2024-11-27 04:23:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 9a5968be-127c-3ca2-a1d2-a9dc2a413515 | -24.11289 | -48.42898 | 2024-11-27 04:23:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b6081369-31ee-32c0-8158-5010c8b33352 | -15.89283 | -43.4617 | 2024-11-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73c22e1d-532b-3147-889e-f9b1597a8ede | -23.36613 | -47.0518 | 2024-11-27 04:23:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 68a55602-246b-32b4-aad0-eade468e1f46 | -21.21587 | -48.64921 | 2024-11-27 04:25:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a71b5d03-f1fc-3391-87f8-cec131f2dcf2 | -20.90932 | -47.3964 | 2024-11-27 04:25:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3441c18-b036-3a52-8f66-199839e9fc65 | -21.34391 | -53.37048 | 2024-11-27 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05d9bccd-6499-3a10-aa84-1df9578d5fa0 | -22.78373 | -43.75763 | 2024-11-27 04:25:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 847e965f-867a-3adf-a87a-51b1ee47db24 | -21.53319 | -45.31055 | 2024-11-27 04:25:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aca27c65-3d45-3da8-86cb-5fd1c4abce97 | -21.00205 | -45.43408 | 2024-11-27 04:25:00 | NPP-375D | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| efcb5817-a7f6-3b35-9674-eda60abc719f | -22.28067 | -48.49002 | 2024-11-27 04:25:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2414da83-9811-31ea-913d-675f91fb2f70 | -22.84856 | -45.81002 | 2024-11-27 04:25:00 | NPP-375D | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14b4bab4-0dd5-3d47-8149-fc03c82f770f | -22.1427 | -50.86121 | 2024-11-27 04:25:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 093f8bc7-c9b0-3628-8344-98ac79bd5143 | -21.44461 | -48.70139 | 2024-11-27 04:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e40e1e2f-d3f0-3c7d-9a2d-5f99de409e57 | -22.13921 | -50.8605 | 2024-11-27 04:25:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8703b30c-b6c7-3902-9465-255634eba328 | -22.14197 | -50.8654 | 2024-11-27 04:25:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 73d0c2b1-a764-32ac-aa29-836a5668d292 | -21.31498 | -42.91306 | 2024-11-27 04:25:00 | NPP-375D | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de3ad224-06b6-3256-9f6e-ee1c40c911b0 | -26.80824 | -48.65846 | 2024-11-27 04:25:00 | NPP-375D | PENHA | SANTA CATARINA | Brasil | 4212502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f49e5fc7-fbc7-385f-80a8-d250e4d57739 | -21.49272 | -46.02794 | 2024-11-27 04:25:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 028b9c6b-57bf-306c-8337-9cd229c2b0d0 | -22.42681 | -47.1625 | 2024-11-27 04:25:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c39ca72-d7d8-3637-8fd1-827e66488ad5 | -29.20619 | -51.89519 | 2024-11-27 04:25:00 | NPP-375D | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7b5fa1cf-4d30-3f55-b9fd-1ae8bc165c51 | -22.11724 | -49.60954 | 2024-11-27 04:25:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6fad958c-42f4-322d-bc6f-6d8e5c86fdf1 | -20.85637 | -49.87429 | 2024-11-27 04:25:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab7180ce-2e1f-38be-ad99-53763777429e | -21.34249 | -53.37784 | 2024-11-27 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ccdec11-77fd-3859-b369-acd059e6343a | -21.33875 | -53.37416 | 2024-11-27 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 180f58c0-8d89-30db-8e78-ebf50301a864 | -27.10918 | -51.46021 | 2024-11-27 04:25:00 | NPP-375D | LUZERNA | SANTA CATARINA | Brasil | 4210035 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aaf3bf3c-d7e4-3e36-8a2a-f5795e99cd58 | -21.19495 | -44.9373 | 2024-11-27 04:25:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9f162355-dc0c-3b22-8eb9-354e87fc01f5 | -22.54053 | -48.81382 | 2024-11-27 04:25:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4b4f7b8-3e0b-31aa-9cda-fecb71200555 | -20.77345 | -47.16324 | 2024-11-27 04:25:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 780d8176-7c30-34de-a4e2-ae8c9eb4bb52 | -22.11762 | -49.61281 | 2024-11-27 04:25:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9ec138c-3084-3687-95c7-c84c686364a1 | -21.3432 | -53.37416 | 2024-11-27 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50e93894-d592-36cc-9689-64e452d9a8b7 | -20.97188 | -47.21217 | 2024-11-27 04:25:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 803fe780-688f-37d4-82c7-2d21906707bd | -21.49329 | -46.02396 | 2024-11-27 04:25:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a05b9f6f-6470-32a0-a60b-53f07ed76382 | -22.11661 | -49.61335 | 2024-11-27 04:25:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b8d32807-36d8-3c54-9e52-c89708713dee | -21.53673 | -45.31118 | 2024-11-27 04:25:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b51e0fc4-f78a-3d9a-9534-02d4ac6e0f3b | -21.33919 | -53.37337 | 2024-11-27 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 960bc377-a1dd-3939-8417-add5223b9455 | -20.9758 | -47.20901 | 2024-11-27 04:25:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README49.md)
