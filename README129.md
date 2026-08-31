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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87fa956c-c3bf-3bb3-8b07-7cf5181ace47 | -3.47921 | -50.58973 | 2026-08-31 16:33:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7ebbf91a-a06b-34d9-aae0-cf4c38025630 | -7.94536 | -44.24682 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a69a6185-f3f6-3191-8a55-01086f63bd4c | -7.04067 | -45.40919 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52ac1456-cbc8-3221-8ab5-4ba1607e25c8 | -2.43582 | -48.43248 | 2026-08-31 16:33:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3f4c3f7d-8a77-3bde-bf55-75abadbe3274 | -6.40337 | -49.93392 | 2026-08-31 16:33:00 | NPP-375 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b45fe386-c814-37b5-8195-314d5067fad2 | -7.91695 | -44.23614 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 36d608fc-3a42-370e-8239-7907c266c003 | -8.06652 | -45.89891 | 2026-08-31 16:33:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82c3c8fd-40cb-336f-8733-61e7faeb2d62 | -6.12996 | -56.38606 | 2026-08-31 16:33:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 975f4861-cf3b-3031-8681-aa63d8fe5b4e | -7.64966 | -46.72765 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 595673c0-f7ba-398d-8ac2-dc80f2d9fe1d | -3.54339 | -51.11632 | 2026-08-31 16:33:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c9abd0a2-23cf-3241-876d-a9b7dd0ca61b | -2.97512 | -44.28494 | 2026-08-31 16:33:00 | NPP-375 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5380e7a-68c8-3390-b44b-f6a7cd99a0eb | -5.25402 | -55.90959 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 056aed74-df6e-346f-9a79-a52edd997596 | -3.71192 | -44.35079 | 2026-08-31 16:33:00 | NPP-375 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75ab8320-37b7-3172-9dcb-d93afd2e1922 | -7.63414 | -46.72984 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1657c483-0405-3338-8439-b5b414178be4 | -1.08646 | -47.8041 | 2026-08-31 16:33:00 | NPP-375 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ecd345b6-8743-36ac-9112-4880f0443729 | -5.85759 | -52.08057 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 30835a9f-190d-340c-93e9-4e7f2569088e | -5.76154 | -44.13237 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 885db0ee-a766-3066-a76b-0b572962b556 | -7.42152 | -44.25695 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 203c2fde-688b-3926-8deb-873e1f7ab8df | -4.08645 | -45.93663 | 2026-08-31 16:33:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7a5e346b-8617-361f-ad7d-4003dc29eea3 | -4.90626 | -37.43693 | 2026-08-31 16:33:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c398d9b5-8c53-38a1-94c8-4c8c933ada70 | -5.84977 | -52.3915 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9ab8ac30-62da-3fcf-9f87-80f80d6f7294 | -5.96201 | -53.61243 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 47b0f679-161a-336e-94bf-d17fddc35ac1 | -7.98523 | -44.3021 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 94d15917-8268-3ed4-aca2-c21916a9e0c7 | -6.69902 | -44.03664 | 2026-08-31 16:33:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 327ba13d-3fad-3a30-89eb-ebe6ea64d347 | -6.94058 | -55.634 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f25189bb-22c0-3ce3-8e68-2fd75adf8f38 | -7.21003 | -42.73828 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5d425390-805a-3b6d-8c7e-3c5e5475f365 | -4.85074 | -55.83188 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 89ec3840-cdd3-316c-9c0c-f292f2c1bdd7 | -6.87832 | -41.6965 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ca748a1f-20e2-306a-a7fd-2c46c7a45e56 | -5.43473 | -36.8636 | 2026-08-31 16:33:00 | NPP-375 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| fc7ee1e5-77e1-3bad-a406-0e6a2e7a20e2 | -8.04927 | -47.27524 | 2026-08-31 16:33:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3e800d0-f1c4-3813-ad3c-0998ab810616 | -6.35223 | -35.24844 | 2026-08-31 16:33:00 | NPP-375 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 09cc1e02-3017-3d70-a4e9-abb8430fa376 | -7.79437 | -44.07198 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 25e82910-5c18-3eb7-86a1-852e1d5c53a9 | -2.84255 | -43.60934 | 2026-08-31 16:33:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 0e926a37-2a33-3831-8265-8c0b5d8edd16 | -4.99078 | -41.82564 | 2026-08-31 16:33:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6b3094c2-a9fa-3ba1-ada6-c08204a565e3 | -6.9132 | -55.69891 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 959bfc9c-b2a2-3d85-abc3-c690bca18323 | -7.03614 | -42.19865 | 2026-08-31 16:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d0ba320c-079b-33d2-93c3-451f6b961d92 | -6.87466 | -43.71961 | 2026-08-31 16:33:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c1ffde5-aab4-31a0-8ca8-60724749d196 | -7.79546 | -44.07939 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 99401bd8-a2cf-32fa-89a9-638dbed1fa9a | -7.42208 | -44.26072 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af52d32e-1082-3c04-a1c2-e5e4e855ee4b | -6.84249 | -41.73091 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a78251b6-1b9c-343f-a01d-c2e2e0288a59 | -7.69342 | -55.33832 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 971ebc13-5331-3153-9aeb-5f5afb716330 | -7.53209 | -44.44312 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 79e803aa-3f58-31c9-947f-dd08b2875a20 | -4.90716 | -43.45806 | 2026-08-31 16:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5078d6af-5ebf-320e-9c4b-361ed40bf26e | -7.63986 | -46.71426 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5dcb572-95ff-33df-b984-d7111de32612 | -6.69824 | -44.0371 | 2026-08-31 16:33:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9db43629-096d-37c1-830b-f4003ade11aa | -7.21442 | -42.74474 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ba4dc66c-6314-350d-91d9-efdbb51cee13 | -7.61893 | -44.93795 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a4ed7369-c6cd-33b2-9fe9-5ad02376c1ed | -6.84545 | -41.68351 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2eea8171-2dff-3058-b659-5e351cdd3ae0 | -7.9499 | -44.25376 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ab88500d-f4b6-38f9-bf43-b19d981a1706 | -2.94492 | -51.96539 | 2026-08-31 16:33:00 | NPP-375 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 005cebd1-f8cf-3b85-8cd2-154a423c017b | -8.71194 | -52.36729 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5c3234df-3934-331a-a952-5ae83f1e0393 | -7.49333 | -44.88847 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d550e9d8-7c86-38ed-802c-a629c89508ab | -7.99967 | -44.28076 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| db9dbd66-bf6c-363a-ad99-4b4e1f3ea205 | -6.13672 | -53.53779 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 61b1187f-33f1-3753-89ee-c8cab4a09adf | -7.35022 | -41.15666 | 2026-08-31 16:33:00 | NPP-375 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6f7c528f-7315-302c-9074-fde8f14ed042 | -7.04365 | -45.40456 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a6b9b8e-65e3-37d7-9eb2-414052f321ad | -6.87723 | -41.68944 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 88c6b8cf-8c21-3ca7-9fc2-8ec75973c958 | -4.30634 | -38.09637 | 2026-08-31 16:33:00 | NPP-375 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 023f39ec-803a-36a9-b41f-0880f5f7ac31 | -4.34948 | -43.83412 | 2026-08-31 16:33:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cbbfccf6-4386-3664-8aec-8b9080a195c9 | -7.09256 | -45.79127 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7571661c-ccf8-3785-abf5-29100d26cba5 | -6.87778 | -41.69297 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a0fdd2d4-0862-39bf-9267-c10d2c30c9d8 | -6.25148 | -53.67979 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5558f762-5459-3748-9c71-4b6ae1c5614f | -6.87334 | -41.68642 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dae49d3b-f973-3ae6-aa45-68316795d549 | -7.02504 | -45.86077 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 16efb378-6f03-32e9-956b-2675890e60dd | -7.42283 | -45.27177 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5580cdea-8f6b-3a7c-bf42-a38fc6684a59 | -5.58505 | -42.32653 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e7691900-3bda-3f61-a7f4-34f6e8c5db83 | -6.38612 | -45.50914 | 2026-08-31 16:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e1a77f10-d5c8-367b-a745-eb7692e1cfb0 | -7.6866 | -55.33931 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 88695720-7b32-3400-968b-a2bf0487958c | -7.12555 | -44.30556 | 2026-08-31 16:33:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb7e29d4-5018-3183-98c8-b2af493d6a10 | -3.59124 | -48.87368 | 2026-08-31 16:33:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ca1f537-7d8d-393d-b359-2821b38feae8 | -1.72425 | -48.29045 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 1d2ddfb6-166b-30cb-9bbc-55d88c42d278 | -7.63734 | -46.72446 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7c23e1a0-f06c-35f0-a12e-7987db524afa | -7.05021 | -45.39944 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d8819be3-ada6-380c-a6d7-7a891ddd5e7f | -7.98589 | -44.28285 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 76e81a4f-b5d8-3e5a-8fc2-6ac2fd3d594e | -7.63346 | -46.72502 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4f1a28f2-8832-3450-9579-aa24e84f7f96 | -6.86355 | -43.9529 | 2026-08-31 16:33:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47514d94-2dc5-3d60-8948-5c56add3a3db | -7.09803 | -45.77765 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a53e92d9-83ea-3341-bcdc-1c51e0503c65 | -7.12897 | -44.30502 | 2026-08-31 16:33:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c031b59-e866-3410-b6fd-18d0e4687523 | -5.57945 | -42.33451 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 847e30f9-27ac-3388-a169-057b565d288a | -8.38531 | -46.46441 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 4dbdba1c-7922-3e33-b1d7-057c57e37ce8 | -6.70203 | -44.84575 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 973c8360-5f52-39a0-be2e-181cab4ec9b3 | -5.46854 | -45.62027 | 2026-08-31 16:33:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74fe7e41-3278-3d86-937c-a764d2b27d8c | -7.56041 | -45.24886 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4cecec98-778c-3e96-9c7f-666b4bdd459d | -1.93997 | -44.76263 | 2026-08-31 16:33:00 | NPP-375 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 03f8c8cd-2507-3b09-afaf-878b40dbf229 | -6.91441 | -55.70107 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d35c6b6a-bdfd-3070-a409-42816c8e5b62 | -8.9445 | -50.76314 | 2026-08-31 16:33:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 77de80c9-bd95-3543-81a5-b8cc27ea1d25 | -7.99567 | -44.27754 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 65207558-24f6-34f7-9b37-dea09a56ef64 | -7.95046 | -44.25753 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d36d2a4-8aa9-331c-86b7-2b3895f5c82b | -8.21188 | -54.94163 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bc0ab3e6-9d8e-38a1-bffe-b6636b6aadc7 | -5.9122 | -52.39401 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| b9dd94bb-4443-37e8-a0c1-4f4e030ccd04 | -5.49077 | -43.67744 | 2026-08-31 16:33:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 71988efd-6342-3684-a3c9-8cad734a1f1f | -7.16769 | -44.68341 | 2026-08-31 16:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8ca8c83-ffc7-392c-8f63-067aa30ccba7 | -2.6667 | -45.31076 | 2026-08-31 16:33:00 | NPP-375 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d514b117-3b95-34d3-ba23-3dda28c7af5b | -7.51991 | -44.45636 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da519603-1914-3726-9b1c-795b6f7a5dcc | -3.25566 | -48.76096 | 2026-08-31 16:33:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eff3ea5c-8711-3991-9065-1f32f9fdb173 | -7.98857 | -44.32457 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6f337722-e180-34e8-b13f-9909d1986193 | -6.84942 | -41.66481 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 91b10d29-11eb-31b0-a22c-ff30443baafe | -7.98387 | -46.52923 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| edfa51e0-e633-3a5a-84f8-3695d22353ac | -7.98246 | -44.28342 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6d28aa34-4b04-361f-9d98-86cc6d87a1b9 | -7.63265 | -44.83574 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README130.md)
