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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fedbe836-97fa-33c3-ae43-029b846210f0 | -20.62318 | -54.83428 | 2025-07-16 05:08:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46969ea6-80af-31fc-a343-605b15500e33 | -20.02794 | -47.39212 | 2025-07-16 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c83b2903-6eb9-3b17-8006-1cb41bac6bf8 | -22.39663 | -49.79551 | 2025-07-16 05:08:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 163def25-4658-358f-be53-402b837cf961 | -20.35113 | -46.54411 | 2025-07-16 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb9c4709-efbf-3d33-8412-dd76c54c7c91 | -20.35185 | -46.55006 | 2025-07-16 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6728ca94-0080-3208-93b9-e9212741d33a | -22.3963 | -49.79919 | 2025-07-16 05:08:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b866d5d4-d2eb-3a85-86aa-55b40a771baa | -16.04 | -57.03917 | 2025-07-16 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31873dc0-a087-36ae-b70d-42d55e9ba6d2 | -16.98762 | -52.00813 | 2025-07-16 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6264485-e223-37a4-a2ea-687d8f79224d | -18.65722 | -55.71921 | 2025-07-16 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4da17644-0ee5-39fc-a571-217baa5983e4 | -17.53058 | -55.64251 | 2025-07-16 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9d0181f3-cb16-3305-a79e-335c88da6398 | -17.91115 | -54.12072 | 2025-07-16 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6bcec33-c59e-3906-9721-f2d4fda7cd73 | -18.58187 | -52.4007 | 2025-07-16 05:08:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b41c9dd5-e610-37fc-96a5-073988aa5d8b | -21.79466 | -52.7603 | 2025-07-16 05:08:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40969b25-d685-3669-aada-dd39c621db0f | -19.74994 | -54.52049 | 2025-07-16 05:08:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff39f1a5-ec88-380e-8bf0-8178e988948b | -14.80468 | -54.2011 | 2025-07-16 05:08:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60ab5e48-26a6-354f-bf8c-a53d35a9c188 | -13.0146 | -45.0593 | 2025-07-16 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 4b6c5bea-bb06-3cf0-ae2a-174d77bd14ac | -6.7194 | -44.3231 | 2025-07-16 05:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e4607a89-cd9b-3b55-8bd5-9527ec7dfd6b | -22.55786 | -54.94754 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b652e5e6-6dc2-357e-aa4a-e4e601f49d7b | -22.57023 | -54.9441 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fb583c2f-796d-3df9-9cd3-6900c60b80af | -27.21484 | -50.66183 | 2025-07-16 05:10:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1ddfc99d-303e-3bd6-9639-716b5bfc8cba | -22.57162 | -54.93332 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e17dabb-51cd-33ab-940a-3fa6be904563 | -22.56381 | -54.93211 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a02be430-36a0-323d-b716-680a58b695c5 | -22.56841 | -54.92855 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0d42560-cd08-3b40-8b8c-bbc93752afc3 | -28.69631 | -55.98062 | 2025-07-16 05:10:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.2 |
| bfdee93c-b8cb-3060-bdd5-a69d25f81876 | -22.56703 | -54.93809 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| be2fb7c5-08d5-3cda-b052-d69806cec451 | -22.5671 | -54.93934 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b73182e-5ce7-3e04-a93d-cdf6796c4d09 | -22.57092 | -54.93872 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 952d899e-e7d8-30e9-9b89-2956259dab69 | -22.55854 | -54.94222 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 53297fde-b32a-3a33-8e0f-ffa36bcee0f1 | -22.55922 | -54.93689 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2b9b6b8e-62da-3ce0-8771-654e2d7e9fe3 | -22.56313 | -54.93747 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d3852a1a-9f2b-308d-921e-4f2ce65d3326 | -21.95692 | -57.58724 | 2025-07-16 05:10:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b91741b-4969-3775-9d24-9696a2f458c5 | -21.95635 | -57.5912 | 2025-07-16 05:10:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dab1e88e-ef70-3f22-b87c-0ea514438513 | -22.21769 | -56.20015 | 2025-07-16 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb36c38d-1611-3dd4-b598-e33b15add26b | -22.56645 | -54.9447 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4dc6a2b5-cdbe-3a8d-97fa-9bec50464103 | -21.95977 | -57.59179 | 2025-07-16 05:10:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62e904e1-1a97-33c3-a05a-b767f3e863dd | -21.96034 | -57.58783 | 2025-07-16 05:10:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e36fc37-26de-3ecb-81c6-67524652b871 | -24.35574 | -50.82157 | 2025-07-16 05:10:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9a62ab4-10cd-39d7-8e0a-5ef5b1e635e2 | -22.56244 | -54.94281 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 9a629cd2-468f-3167-b9ec-a779f85412d8 | -22.66293 | -53.38085 | 2025-07-16 05:10:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bb8285e8-d6a2-309b-bce4-bc2ea7a74d40 | -22.57166 | -54.93457 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36083226-7b59-3b92-a88a-22e44bab9cad | -22.66069 | -53.37894 | 2025-07-16 05:10:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 91d2f8a7-5415-3a13-9987-e33ff9d78d03 | -25.85543 | -50.40023 | 2025-07-16 05:10:00 | NOAA-21 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| af87be5c-fbfd-3689-8340-282412a1f6c8 | -22.55991 | -54.93153 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0492a3d4-7338-3f3b-83ac-763e245049ca | -22.55464 | -54.94165 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 85842cde-f32d-3ad7-b159-c20e493087a9 | -22.56776 | -54.93395 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8eb410cb-af73-393e-a272-3f3ad4244a5d | -22.571 | -54.93997 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ca477d5-be8b-39b0-945d-2e514032aae1 | -28.69827 | -55.98026 | 2025-07-16 05:10:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 98bfba18-d268-34b0-8278-b31ca88022ae | -22.56771 | -54.93271 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a8e6930c-5b20-3efc-860c-4e412a3541bf | -22.56634 | -54.94345 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 3e7a94cc-fa81-3cb2-8d28-697ceb462375 | -22.56176 | -54.94813 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ca0dc82a-7503-383b-ad5e-68b2e637fa4b | -22.56566 | -54.94876 | 2025-07-16 05:10:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 92e66917-73de-3fe2-9ec7-4b7a6c590e07 | -13.0146 | -45.0593 | 2025-07-16 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a28a5647-2578-36ad-8607-5e0e4ca4e2ad | -6.7194 | -44.3231 | 2025-07-16 05:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6f8a85bb-6c62-3ffe-975a-6a0418255548 | -3.38392 | -47.4917 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2a66690-9698-31b7-8212-668aa11534bc | -3.38595 | -47.47745 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89f3720e-65e9-3bec-b0b8-6c2fe8c1d09f | -2.584 | -51.92201 | 2025-07-16 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22137c5f-810a-39c4-bce7-b766b7359bbe | -4.30198 | -48.09638 | 2025-07-16 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b420a141-c90a-34bc-8682-e73074021606 | -3.38492 | -47.48465 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac21ac50-7277-3839-8e43-e7b574f69473 | -4.03446 | -48.06034 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5dabcf88-7a9b-3c2f-be6f-59b2914db31a | -4.02641 | -48.06607 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bf2d837-16d5-33f3-a4a7-b65001db8396 | -4.03226 | -48.05802 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a45f0ee-36a3-385b-a105-75a74f16d040 | -2.91949 | -48.23734 | 2025-07-16 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b3a87f9-7919-3c2e-8ba3-270c4ebee9a2 | -2.92638 | -48.23844 | 2025-07-16 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a31ebfee-83b5-30a7-9171-24acc79796d8 | -3.03725 | -47.86437 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29a2b3a8-9344-3a86-92f8-c435b21ec4b7 | -3.03312 | -47.86101 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b294f1e-caa3-32cf-a8b9-48480398622e | -4.10914 | -48.20541 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e83e240-e5de-3e00-ab96-9e4754bda531 | -2.91166 | -48.2426 | 2025-07-16 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b17f3ce-18df-3f97-889b-87286e54d162 | -2.44849 | -47.32688 | 2025-07-16 05:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 082bce13-1105-36cd-af99-7035768c4a43 | -4.02744 | -48.05903 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 796201b6-cd7b-3e51-ba34-679661512259 | -2.92707 | -49.06401 | 2025-07-16 05:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaba32c6-de69-3411-ac43-3a2237b0afaf | -4.03128 | -48.0651 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 32a1be78-c4d5-33a8-9a8f-8d478d5d4bb9 | -4.11169 | -48.20686 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbc4e9a6-e947-3bd1-b697-f96f9e2d40aa | -4.30102 | -48.10315 | 2025-07-16 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 491860c4-af2d-35f0-b31e-f0d5ab6d804e | -3.44523 | -59.21588 | 2025-07-16 05:29:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9c5a317-26f3-3f8f-bd44-50b8184dfd29 | -2.9126 | -48.23629 | 2025-07-16 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdc874bc-f73f-375c-9f23-63cd45ca8a16 | -2.91856 | -48.24361 | 2025-07-16 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c95df5d1-a64f-32a3-b767-4f798d0e9de9 | -4.03347 | -48.06716 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de512833-f81d-3bc0-a2e9-55e0011579c5 | -3.39115 | -47.49282 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c300f57-01b9-3365-8ba6-36f3081e62f5 | 0.76709 | -60.49482 | 2025-07-16 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72031227-7b8a-345b-906e-5820b5e2649b | -3.3847 | -47.47965 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7aa6b5c-df15-32fa-9c0e-3ad74ee50c10 | -3.38982 | -47.49492 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc3ec739-7b43-3c90-8a08-24dc73c8cdb1 | -4.10467 | -48.20587 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61924084-02ac-367f-923e-e625cd9547d6 | -3.66514 | -50.95208 | 2025-07-16 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c334a06-a555-3043-82ce-db1e9d986f97 | -3.3826 | -47.49376 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c7864e7-e9fa-3347-9afd-f64aed58664a | -2.44128 | -47.3257 | 2025-07-16 05:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf701341-694c-3aee-9f48-82dee068a5e7 | -4.03834 | -48.06615 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 585a8872-081f-3b57-a408-21aa636635ac | -4.03036 | -48.07171 | 2025-07-16 05:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b589ca6e-dd5b-3e24-b6c8-5a5fbf0bddea | -3.03217 | -47.86728 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f41c8ef-8647-301c-8997-304dae80b519 | -3.0302 | -47.86324 | 2025-07-16 05:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99266cb0-07e0-304a-a3e7-f9162f8b1ea7 | -20.0798 | -47.6553 | 2025-07-16 05:30:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 689fa825-545d-3184-9f9f-e1e0877c0b1e | -6.7194 | -44.3231 | 2025-07-16 05:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e6f62e65-a2bb-3078-b6e5-fd150f04930c | -20.0805 | -47.6319 | 2025-07-16 05:30:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c0534e94-0e3e-335a-8a9f-475f957b1248 | -13.0146 | -45.0593 | 2025-07-16 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b0ae6f61-ebf6-3685-bdc4-ee1211fe9ef5 | -10.06182 | -59.10421 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c62ef9e-2399-3ddd-b0d7-c3039faff895 | -9.7086 | -56.18515 | 2025-07-16 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03f887b1-655f-33f7-8e90-eee794cbc4e0 | -9.96487 | -64.96017 | 2025-07-16 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7735376-6831-3d7d-94a8-83361d32a415 | -10.05833 | -59.10153 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b6e808c-5694-33f5-af03-743157bc5003 | -9.62591 | -67.20884 | 2025-07-16 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fb24f88-f525-3d9f-af8d-b3ba05629fa7 | -9.65901 | -63.2202 | 2025-07-16 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd90f822-51fb-327e-8d0d-b98874ed552d | -11.87519 | -58.70993 | 2025-07-16 05:31:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
