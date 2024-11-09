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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5477f32f-a944-3f24-9c6a-38a236b81e61 | -1.51849 | -51.30717 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39d32fd-c69b-30dc-838d-daee6939651f | -2.24873 | -50.413 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca554f3-c35d-3a6e-bda4-369aa8e9d41b | -0.36287 | -51.41509 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eed2d305-4e66-3cad-9556-bd635bd07e87 | -3.44931 | -52.71997 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7ae5056-083a-3d17-9a34-d7c1ae5ff251 | -1.52449 | -52.16107 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0f943f1-6677-37c3-bec7-8622dfdbf4a5 | -3.5857 | -50.27786 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16026630-02c8-35b0-8bed-8d7b36a60ef6 | -2.31609 | -46.47773 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8843d8a8-066e-3da3-8f80-0b152bcb2ad1 | -0.90565 | -51.76754 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d348396-69ad-3f46-9876-94e7ed0171ae | -1.72045 | -52.4655 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4f6ae22-d2a1-33b9-a7e5-7e5bd07d691a | -3.27632 | -53.67405 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c8b0064-74e0-38a8-956f-7497a7f1390d | -1.59653 | -52.1505 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee04cd69-384d-37ad-877f-bc1997e32a67 | 0.63069 | -60.09152 | 2024-11-09 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebf84f2d-8e3a-3034-a3eb-8292df659330 | -3.60817 | -48.91945 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 61cf2ba8-97ec-3ba9-a5a8-70c4cb5ffeba | -2.98876 | -51.45741 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2520f14d-8664-35e4-91de-34dffd4dd3ad | -3.35307 | -50.12024 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ea4fb015-88fd-3885-90a9-8eb047ea401d | -2.40954 | -50.30898 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18c9c9f5-dad0-340c-ba6f-543bb242b9b4 | -3.24759 | -50.44781 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17b60262-fab6-3c29-bc43-fd05fd7e6875 | -4.21535 | -48.68279 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 183a79a7-ab50-3434-a7bc-2b7bdd52b45f | -1.51393 | -52.16301 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5d900d5-a122-3413-bc93-1403ca306df0 | -3.23133 | -53.39856 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 597bbbe4-375f-3425-91a8-fdab7baf815a | -2.61668 | -51.74471 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77236ad3-d4e4-3557-8f83-6a4196316e4a | -5.81083 | -44.11934 | 2024-11-09 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 896bb36e-c591-372b-93e8-be1c3a172e91 | -3.17464 | -50.21457 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57b7e53e-a7da-3081-ac74-bf2f683728fc | -2.73175 | -51.74355 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 627967f1-df1f-3316-b182-f827393427df | -1.50446 | -52.15796 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1271644f-45f1-3ad0-9d36-0301d950cfc1 | -3.76696 | -51.34336 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ef609ba-288b-3a0c-b923-5fc5398e7e9f | -2.17399 | -48.33217 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc7f48d3-5469-386e-ac0f-7dfe63d45448 | -3.18044 | -50.24963 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40e674bb-eade-3039-a3a9-0c43c366522e | -2.23078 | -46.54495 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b371d02-bc3e-3737-87df-b47dfee8e49a | -5.67524 | -46.99438 | 2024-11-09 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a81806f2-e46c-37a2-9b1b-5dd329bad4c8 | -3.33892 | -45.16236 | 2024-11-09 04:55:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72dff242-0609-373f-b56d-cc501819451a | -2.20503 | -51.94154 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71b30266-92c7-321f-b0a6-fbafdadf052b | -4.21112 | -48.54528 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b579dea3-2f4e-3223-b19b-e6eb4d430164 | -3.17047 | -50.21577 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 585bcc2d-b493-367c-8087-ba814686c1c5 | -4.10917 | -48.85905 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c7d3b99-4873-32b0-90ce-bb9d6b6db529 | -3.52934 | -50.86801 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e76fdfc6-3e7b-31e0-8d82-cc639a638670 | -2.32934 | -50.44853 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0831bfb-e710-3cb1-9444-120531b4b4e8 | -1.46616 | -51.99429 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d97fc84-9637-37a5-9306-bc657a215888 | -6.23098 | -47.27814 | 2024-11-09 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5d79253-13e5-31f8-b686-0e9f5ed36eeb | -6.1337 | -42.56284 | 2024-11-09 04:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 86241b72-c1e1-3618-ade9-0435e1f90f1d | -3.84634 | -50.04024 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b995cdcc-5e0e-38d4-af42-6af8d655e390 | -2.69576 | -51.70515 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7c37f2c-c679-32b3-ad8d-c86a2d40ef40 | -2.95246 | -54.45222 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c75fe637-ce16-3d72-81b3-afb0f036ec87 | -3.71576 | -53.39678 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a359f7b-c721-3c77-a5e7-cc7dcca868a1 | -4.29194 | -48.58649 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9a9bb45-7c0d-39e4-b661-607f6cde28bc | -3.03757 | -50.41891 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 176a7e8b-4761-3639-8caa-145e6da2197e | -3.5944 | -47.35044 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 931b871a-9634-3721-ad99-2fa8fd9c9cbd | -2.40916 | -48.39993 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 221367c2-fea2-3835-a454-99ce66276dd0 | -2.23496 | -48.36919 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd5594f2-0fad-3a39-8eae-f87f7c43a972 | -2.87471 | -53.96568 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c02d253-651a-3593-bf19-ff056b3f6e20 | -3.06737 | -54.16039 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7252f41-2dbf-306d-b422-938d36142506 | -1.15094 | -53.64986 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f2134b4-e9ff-342d-9504-16c017ca617c | -2.58622 | -54.00997 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ac89f20-a0a4-30d8-9395-73645e83331c | -2.18997 | -53.63147 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1126f21e-b3c9-309d-86b1-a5a18fce52df | -1.33987 | -52.19647 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c792e3ea-417a-330e-906e-b4ba0baeb885 | -2.35899 | -54.75654 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c403d0b1-0b3d-396b-98fa-4af37d4231f3 | -2.04874 | -51.9611 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39141b4c-d3cb-3b06-a71e-1700b4fb2d74 | -2.91316 | -51.05099 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b7972b-88ca-3f8b-946a-a4a8c6f21c62 | -4.21063 | -45.85575 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71fa2459-50e5-317f-9400-bf336108e5a4 | -2.58124 | -53.98452 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3714fc51-343a-362e-a16d-6be040505a43 | -3.02642 | -51.5312 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ad00445-8b74-31c7-8aac-5b8438544abf | -0.22172 | -51.64365 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d348c583-bb17-389d-83ab-6572e5d5020e | -3.12802 | -51.10635 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c302749d-ff2a-3cde-bb84-8851a20e8ec2 | -3.59119 | -53.09381 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d46f80-75e0-3346-9476-2bf5aadfe1d6 | 0.62929 | -60.09019 | 2024-11-09 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4bd6d12-25ed-3633-a67f-2a878aabc58e | -4.77909 | -48.67852 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45c96957-de6d-3129-8543-5be2b03500fb | -1.36721 | -49.357 | 2024-11-09 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24ef7090-5301-3ace-8c6f-b70c3971e9d6 | -2.63736 | -46.03617 | 2024-11-09 04:55:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcdb02f5-69aa-3b06-82b5-290044ed91f0 | -3.00963 | -53.4312 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ae5e159-7159-3cc8-a2bb-6427c8fd330f | -3.16005 | -54.48785 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| db5bae0d-001a-3a16-83f6-74837a7fb474 | -3.07988 | -50.56111 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 45aa0ef6-a59a-32b4-be6f-66ab339859a2 | -2.45721 | -50.39341 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b4b75b6-14c9-3539-a1ae-71baa387289b | -2.65309 | -48.56025 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9f4a4ec-bbbe-395e-8a0b-3060dad12d2b | -2.0791 | -50.33896 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 158baf0d-569b-3dba-b579-738464bf444b | -2.94818 | -53.92792 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4da1f863-1997-3cdf-8d32-b8fbe8f3006f | -4.09135 | -48.51307 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 937ba4c0-8664-349e-b5aa-5af5f693e469 | -1.83307 | -52.26269 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa362353-0927-335c-85bc-68fca0b3c759 | -1.23541 | -51.75626 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d758f5-d9de-30e6-bf1a-4ff06242eddc | -3.59361 | -50.2748 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97d09673-c88e-3205-9e81-f7b4796edf08 | -2.85847 | -49.22314 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f03dadc2-d0ac-31ef-85fa-ac2e770d8610 | -2.36015 | -54.74929 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd8c1801-336c-3fdf-9d71-dbb99c9be03a | -2.61612 | -46.15975 | 2024-11-09 04:55:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 635e94eb-db3b-3309-afc9-3b76452d3d5e | -6.17865 | -45.44727 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15989523-5b01-3a51-a854-4c5ba94dea19 | -1.15208 | -51.99244 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 574a94a7-d94c-3bc3-ba99-699e831f10ad | -4.38855 | -48.57637 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 020ceccb-c10d-33b2-ba4c-c9436c2fdbb6 | -3.08158 | -50.57361 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 064a5851-e0a0-3056-81ab-40302b095311 | -2.86324 | -50.32705 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bfe7cdb-4027-31a7-ae86-82a3c17e4648 | -1.14047 | -53.71607 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 859b3a41-cc96-3279-be88-e5210d5ab861 | -2.79849 | -51.49269 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df0d4b88-b7e1-3c48-90fe-fe45a7d550a6 | -1.67375 | -52.05125 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 153b7491-ec84-31a0-9992-e4e73f409141 | -2.76715 | -54.04902 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a008418-140d-3296-ad80-49ce994a3712 | -2.17981 | -48.32919 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98f01988-dc1f-3e3b-97d7-1a6f7b7da293 | -4.12668 | -43.58846 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63791452-83bf-3e73-9499-b9bd4c49c2e8 | -3.62401 | -54.10849 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e8437dc-567d-3400-8e76-b660e0b25d03 | -2.31539 | -46.48229 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d16a5a1-c9ba-3a46-8c54-4827d0d961f9 | -1.34141 | -54.60904 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 583e1989-b9ff-3ccd-ac98-7a83cf802e36 | -3.96967 | -48.16528 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02242f5b-fd2b-3acd-aa2b-9b851c450659 | -3.03687 | -50.30608 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cc68242f-46da-3ed0-b56c-5e7970fa64bb | -0.84577 | -53.03212 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06363f62-7c78-3eee-b0bb-29aedff87188 | -3.18068 | -50.58332 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README86.md)
