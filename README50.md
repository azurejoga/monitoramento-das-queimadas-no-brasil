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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 844c4ad1-2f06-3168-88bc-52026016e299 | -7.64246 | -46.11323 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 815c51e5-de61-3dee-b4da-79e95e86ed7b | -6.9911 | -42.17803 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b6324641-a4af-31f1-a190-bc98e2711418 | -1.62022 | -48.28599 | 2026-09-19 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65e6c525-eff8-382e-b375-c7bd50167599 | -8.76673 | -44.24516 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1377a314-2eb6-3eee-b9c5-d364a3b6de4e | -7.50605 | -44.90619 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 282bcde1-1646-3877-a98e-548adafc12d5 | -5.88182 | -52.05046 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c3a822e-dc7b-3586-bae0-a5511c037dd0 | -3.37108 | -50.45282 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 366df8b5-eec0-3a93-bd8e-523c4116a481 | -7.09978 | -46.44484 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e88c737c-f054-3232-9409-581b5b28f8a8 | -6.77657 | -47.8582 | 2026-09-19 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7277f9bc-6b19-31fd-aa51-2cd82a359ea5 | -3.36876 | -50.44191 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3967fe2f-500e-31fc-b6a1-776aa16348d0 | -8.47414 | -47.01097 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15f62e64-68e1-39d3-88cc-836284aeca71 | -3.46148 | -50.61182 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f76161de-fa94-3339-bfab-8cc052f8d7c1 | -7.36309 | -50.32451 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e44e340d-e609-3a95-969e-9adff596d0f5 | -2.90077 | -57.79436 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26a21565-63cc-3642-a044-cbb7fa615beb | -3.02759 | -51.3361 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 456af0da-fd98-3320-adf2-fd942090aa80 | -4.56498 | -42.97366 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5ff63f0-3a40-3c04-9be9-e35d21d2f85b | -8.81642 | -46.9444 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 778fabdd-1c87-3f9f-bdaa-1d5230b4d9c0 | -8.63659 | -47.54119 | 2026-09-19 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cda8fabe-3822-307b-bac6-63e465fe0b0a | -6.6722 | -50.90038 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7061cd6f-117e-33c8-b712-d318d4e001ad | -3.23429 | -46.947 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa6c36ab-4b53-30e5-80ef-12aa6202f56a | -7.95352 | -44.03083 | 2026-09-19 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7d56a3d-39c2-33c3-bd2b-ab5517f5fcbf | -7.19612 | -50.83271 | 2026-09-19 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3af6e44e-6939-39b0-804a-c485409be7ff | -3.35991 | -50.44574 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dcf7774f-6fc7-320b-a0c3-7a5ccceb7114 | -7.75541 | -46.72453 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e923c91e-fd36-35b3-9296-d87269bbf713 | -2.82561 | -50.46181 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 37ff3050-3c9c-342d-9951-b92f454df8a4 | -2.89792 | -57.81097 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5ba8047a-e1b8-33c5-a132-a8cfb9a05814 | -2.73356 | -49.46185 | 2026-09-19 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 82f90f2b-0d21-3123-a753-c655a8f1c9f4 | -7.48472 | -45.28903 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5397512-7dff-3725-9e61-181b0596d825 | -2.89981 | -57.7999 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ce9e99ef-7bce-359e-91ea-523f0953c925 | -4.68412 | -46.39902 | 2026-09-19 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d702a3f-46ee-3579-864f-640b665790b5 | -3.21049 | -53.95112 | 2026-09-19 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24cea878-d88d-3215-a9c5-702497d900d4 | -7.76428 | -46.73309 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39c98acf-8e18-3d9d-be57-92ffa1886795 | -3.36602 | -50.73892 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b6ac044-d919-3de8-9362-be1413dcae00 | -6.00304 | -51.79784 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64b14424-766f-303b-848c-02663e9cdd4c | -7.85847 | -44.86135 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86d2ab20-9c60-339b-8de0-7508839428d4 | -3.2059 | -53.94734 | 2026-09-19 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 072da7f3-6e80-369b-8053-70ca46587082 | -7.77369 | -44.86768 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5e1ed74-df7d-3a67-b66d-800f2819d3f3 | -1.71143 | -54.88966 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d760690-e337-3d15-95e4-ca0d2b9db6d7 | -5.63472 | -40.8682 | 2026-09-19 04:38:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f4e661ae-be45-352e-b6cd-015f25d34b7f | -6.31828 | -45.60741 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4e6907b-7e83-3408-94a6-1eb9700ed8ee | -4.06151 | -56.25077 | 2026-09-19 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dfe8825-9645-3092-89a5-64cedfde3504 | -5.2352 | -47.56162 | 2026-09-19 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4348b13-370b-35d0-83e9-ce0df775bbab | -6.4205 | -46.20178 | 2026-09-19 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eecdf843-fc86-32ea-a3a1-c37efe934242 | -7.22102 | -49.63625 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a3a9a6a-6368-3b56-b467-cae4617de61f | -8.37415 | -47.21753 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f08bb7f3-6817-3f53-a899-320db42d68e5 | -5.2284 | -47.56053 | 2026-09-19 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8a6c832-bbaa-3669-a548-2b36aca2a3b5 | -7.77825 | -44.86087 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bfc015a-9ab5-3703-bbf0-3913e0a279c0 | -4.50244 | -54.97696 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1321c003-89ba-38df-a96b-7d1d74dd0963 | -7.62953 | -44.73945 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0e199dc-abbc-3a12-bb20-6755c764901e | -6.65314 | -50.91778 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 277cf491-a19e-3730-8df5-36e736184893 | -8.12586 | -44.82583 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50635f89-b4f2-345d-91af-c52ac7544486 | -7.76483 | -46.70817 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 139e5bdf-348a-3604-87a3-beeadc557b9b | -4.36126 | -47.78293 | 2026-09-19 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75874e36-337e-301c-8365-05f632cd0c3c | -5.64882 | -43.39504 | 2026-09-19 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8fd17af-3044-319e-91d8-21754cde4029 | -3.04313 | -51.37554 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c134ec60-6845-3026-a2d7-b536f43a4d72 | -7.37289 | -44.73114 | 2026-09-19 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 368d7b3f-43eb-392d-bc38-3ed46753a088 | -7.52931 | -44.93615 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 554013d7-2293-37bd-b672-28a45749032a | -2.81637 | -50.46758 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2017767-4b56-3089-ad1a-3586adc528d5 | -5.84401 | -44.8961 | 2026-09-19 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed544dfa-d2f6-3d46-a943-a63c4441b3dc | -3.36236 | -50.45582 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d36fa650-835c-352f-b285-8861e3dc2000 | -7.69073 | -46.08865 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0578c696-e6f9-3293-a0d7-3adaf659a5fd | -4.84956 | -48.31018 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f96eacb-1c55-33c9-b488-376932d40477 | -3.02468 | -51.19439 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3a7b664-fb3c-32c3-8360-66db4db4c1dc | -4.49122 | -54.97824 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc38466b-7489-37b3-9c46-83726cb2d508 | -3.45744 | -50.61115 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed06c9b1-9f98-3f9b-8b12-0f88e9219968 | -4.57654 | -42.9463 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc99ef09-0011-34f6-a662-c5b0d7325697 | -6.58357 | -44.15339 | 2026-09-19 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf1a1f52-222b-349a-b1fb-08588f96d445 | -3.8378 | -49.12888 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b200508-3466-330f-9f1d-cb81b62124c1 | -8.12774 | -44.82923 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76c56330-22b7-3bdd-963c-52c6dda53f8a | -8.85868 | -45.94425 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5e2050e3-faa8-30a7-a253-7157664c9c78 | -5.40749 | -42.94493 | 2026-09-19 04:38:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 34546d07-2267-38c0-a1f5-b44834edcc9d | -7.49753 | -55.01339 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c0ae3df-5d42-3768-8529-552e87c19b57 | -4.14609 | -48.22168 | 2026-09-19 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00234de5-cad4-3414-9d00-660c4deae605 | -5.74614 | -57.60115 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d8f3c36-6029-33b7-ad95-05ac4c6d38e7 | -6.97883 | -42.18097 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2bf803d7-32d6-3cd2-bdbe-fc0ba4756a5a | -8.88044 | -45.93682 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66b621b6-cc26-33f6-b6cb-392391cde4cf | -6.67137 | -50.90539 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2e8f513-2666-3753-a014-086d2ab2799e | -8.66021 | -45.44786 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6931cf7c-bce6-34b3-a788-bf67ee03e691 | -4.82484 | -42.88071 | 2026-09-19 04:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9f3e56bd-42f3-3adb-a1d2-906feed79be5 | -6.0207 | -51.76934 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f00b09c8-6ada-3a3d-a5ba-d166582ba4ca | -7.86444 | -46.44556 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e534db3-d4df-3a86-9ad4-75592cdaac22 | -4.49537 | -54.98627 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04643185-7eb6-3a53-b3e5-03f34e634aa9 | -4.55719 | -42.97665 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eb26c54-51ed-3d2c-9b34-78ce1187f240 | -2.89326 | -57.79875 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 396d38a6-0970-3dd7-ab64-bd7d118ec6c1 | -5.89388 | -53.56168 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf7d59b0-58dd-36fd-8711-b64ae8690d20 | -2.66116 | -49.4812 | 2026-09-19 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 73453058-08a3-3744-9882-6e4718e835d2 | -4.50304 | -54.97338 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61701a2e-1e36-35bd-bd40-7dfef3489560 | -1.64009 | -55.14983 | 2026-09-19 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97be4498-9f54-37d1-9577-d591024ff045 | -5.2318 | -47.56108 | 2026-09-19 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0621d298-89fc-3031-954b-f6499ce78eed | -6.02625 | -51.76566 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 791e080c-b273-3786-a388-3fe2b0cb1e80 | -4.40877 | -55.49854 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49c9dc80-7eaf-3e44-8736-c3c265a12ef6 | -2.81579 | -50.47111 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4987a757-03f8-397f-a30f-832dc5f1e40b | -3.03628 | -48.41137 | 2026-09-19 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 847743ba-a926-32fd-8b71-bcae30162975 | -7.04524 | -42.08486 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ddedb656-285c-3d67-9911-ce836c2b23b1 | -5.3005 | -50.08713 | 2026-09-19 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69d6b5aa-02d9-390d-a0e9-460c37607174 | -6.23306 | -51.7137 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 041aaefa-fbe1-304a-abc6-fc05568d5fc9 | -4.50676 | -54.96652 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dafb3331-c247-3118-b76a-0bd65749d699 | -7.6342 | -45.82471 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1558897-c121-3c25-adaa-18b8481530f8 | -2.81925 | -50.47532 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccddba7e-c322-359b-80b8-64f0f8b2d2bf | -2.90447 | -57.81215 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README51.md)
