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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dea4c476-9779-3cde-b27e-5939eda2304b | -9.66788 | -43.89825 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e8debfc-cbac-31f3-a53d-d397c7f6ba18 | -11.04217 | -45.40132 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdf02627-e644-33d4-9a94-42f6410a7cb0 | -9.67367 | -43.90795 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f43c6ae2-6933-3e07-8c7d-8c43ce32e38c | -12.61882 | -40.52419 | 2025-11-11 04:01:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5bd156b7-2c0a-3e58-a654-c3ffdad6c044 | -11.5458 | -44.08325 | 2025-11-11 04:01:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 136d5073-8833-31f7-87e9-a3b766c72396 | -9.66716 | -43.9025 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 35dfd2b5-2a3c-31c5-b79a-b77b7d713e51 | -12.4054 | -43.8037 | 2025-11-11 04:01:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f97b3f54-c861-3ef9-92c4-e5248d9d50bb | -12.33498 | -43.65948 | 2025-11-11 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb1ca739-6309-3eee-84ae-901d764035a5 | -11.72996 | -43.84917 | 2025-11-11 04:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91d05a03-a13e-3331-b48f-a1fc09800bea | -11.90795 | -43.82453 | 2025-11-11 04:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7655632-2c39-3668-9fab-e9e5d5e7ff77 | -7.51383 | -41.83619 | 2025-11-11 04:01:00 | NOAA-20 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 601abb26-c0df-3695-9d58-0af5cb124469 | -7.27909 | -45.05434 | 2025-11-11 04:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06007ea5-4211-3e42-9528-9eba303556d7 | -13.49783 | -43.04422 | 2025-11-11 04:01:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5a0e0091-ceab-30c5-8c14-879b498bdc91 | -7.59535 | -43.686 | 2025-11-11 04:01:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 486f39ce-e5f7-3523-86b2-ab9bf77b1e06 | -9.97963 | -44.45663 | 2025-11-11 04:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dac7de0-d2d8-3e30-9742-383f913dd8a5 | -9.3779 | -36.04039 | 2025-11-11 04:01:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f704f096-5fc8-3b48-a68b-c90ef83426d4 | -9.66786 | -41.16792 | 2025-11-11 04:01:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 458ae042-db78-34d2-bd26-f3e9a2e27852 | -10.84942 | -44.94365 | 2025-11-11 04:01:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89bc79ac-1edd-38b4-aab4-42e45772b61a | -13.49446 | -43.04364 | 2025-11-11 04:01:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e5c03dd-f017-3b48-96b3-194834b03f1f | -13.53978 | -43.63742 | 2025-11-11 04:01:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1294c8be-cb55-3ec4-b50c-8561915aeee4 | -11.04601 | -45.40205 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 293b7b92-0b7c-3d85-8b3c-a6b1609612c2 | -10.70556 | -44.78814 | 2025-11-11 04:01:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6fad4e0-b8be-3bed-9c36-6b6b59c77d69 | -7.29326 | -45.06756 | 2025-11-11 04:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c42cabb-30a8-36c5-88f4-fe26703134c0 | -11.54648 | -44.07913 | 2025-11-11 04:01:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93e56235-d025-37cd-81cc-2fd31cbd6c0c | -13.46289 | -44.03198 | 2025-11-11 04:01:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c55bb7b-79aa-3754-8a1c-49b9a0266ad1 | -13.53722 | -42.99423 | 2025-11-11 04:01:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18fdaf93-a860-3c80-96f6-364a06c4f544 | -12.33845 | -43.66008 | 2025-11-11 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90ecd29a-0354-39a4-8be3-66d2a2eae70a | -11.04131 | -45.40624 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4dd3bba8-f76b-3ea2-af02-0f65e523554e | -12.32804 | -43.65827 | 2025-11-11 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd103d47-73ea-3fe2-b6d7-e9cf24400cd9 | -14.17715 | -44.20914 | 2025-11-11 04:01:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8f704dd-238f-3fec-9770-14406c8dc612 | -10.15232 | -36.24929 | 2025-11-11 04:01:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6a2c54fe-adac-3ab4-9cab-77bfc3c6689b | -11.68744 | -44.88594 | 2025-11-11 04:01:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efc9c00a-c59a-305e-a414-bc43699152bf | -11.16937 | -43.57786 | 2025-11-11 04:01:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49a7d016-441a-3d72-b8e4-fc449076170f | -12.01262 | -43.85007 | 2025-11-11 04:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10d6e55f-ed80-387f-a5d8-388aab9fa11d | -9.38181 | -36.04096 | 2025-11-11 04:01:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a718d3ab-cebd-3a2d-a334-f294d7b60ef3 | -10.1516 | -36.25425 | 2025-11-11 04:01:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8b6b61e5-76e4-3b5f-aeb5-8791e35cd4a2 | -9.67297 | -43.91209 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 361fe77e-a874-315f-a37b-4e9c6346a34e | -9.80291 | -43.94167 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32bdff22-bbba-3487-a4f5-76bdc39c0261 | -13.51665 | -43.71235 | 2025-11-11 04:01:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0090433-3d4a-3a45-a9d5-04eddd9f5a90 | -9.18704 | -41.02938 | 2025-11-11 04:01:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22bcc213-420a-36ae-95db-f3676580e9fb | -11.05155 | -45.39307 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17770920-1752-3439-94c4-fc835dbbfd76 | -12.56849 | -43.90876 | 2025-11-11 04:01:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38bd5377-e226-3924-9eea-9a4d2daec7dc | -9.88782 | -47.86626 | 2025-11-11 04:01:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eea8d48-3c98-343c-87fc-314f2746d513 | -7.29666 | -45.0717 | 2025-11-11 04:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c3c67f1-1201-3a11-b65c-262bd36e6023 | -7.29386 | -45.06408 | 2025-11-11 04:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5aff7c3-57fa-30f3-9d4f-1b7fb1b38748 | -9.09742 | -35.4104 | 2025-11-11 04:01:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1f51f818-b266-3bef-a0ea-73aa8795b060 | -10.93484 | -45.08152 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60ebc988-e4ed-3d33-92ea-9de7b56fa5d4 | -12.33216 | -43.65497 | 2025-11-11 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a473f674-6c38-3d39-9b8e-3c0c797f3673 | -9.89244 | -47.86707 | 2025-11-11 04:01:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f15229f-2277-38ab-8c98-9b41d2774578 | -18.47415 | -53.40047 | 2025-11-11 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 99189a5b-50eb-3aed-9dda-f2ada6a640f4 | -17.5607 | -54.01893 | 2025-11-11 04:04:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b606209-a1c9-3d29-96b9-0de0d5def308 | -18.39197 | -54.98553 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 642c90ca-4a21-341b-8e29-a2d219861037 | -18.03405 | -46.78059 | 2025-11-11 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7957c4dc-8231-3c0c-abb8-80dd703d7577 | -18.38984 | -55.00513 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ee1cdec5-40e0-3932-b909-869fbbe82ef3 | -20.79189 | -48.35555 | 2025-11-11 04:04:00 | NOAA-20 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ba0e772-9821-3c4c-9855-db303d04ac98 | -19.74646 | -58.06258 | 2025-11-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 13963ed7-4d79-3757-adbb-71ee098238c4 | -20.13754 | -45.75065 | 2025-11-11 04:04:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00cf0ebf-e775-3cfd-b566-233aa04add0a | -21.40751 | -45.33822 | 2025-11-11 04:04:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6f49b565-af3c-3183-a9d0-a20d320e655c | -19.75764 | -58.0178 | 2025-11-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e8280c0f-d8b3-32be-9ed5-886519f04de3 | -17.55966 | -54.02369 | 2025-11-11 04:04:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bad3f12-036a-3fbb-a96a-f530511669fd | -21.41716 | -47.67426 | 2025-11-11 04:04:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e57de100-6aaf-36d8-b350-5cf7a34b981f | -18.39314 | -54.98045 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73bcea87-eada-37ff-9ae7-1fe76bf19340 | -20.13826 | -45.74651 | 2025-11-11 04:04:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e43dbbba-56d0-3a78-b38d-9e4f72bc351a | -19.75241 | -58.02714 | 2025-11-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 46d383a4-1f5f-3554-90b9-011765120120 | -19.75423 | -58.01966 | 2025-11-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 008957ef-2666-3417-b487-aa4ba7018694 | -18.39098 | -55.00001 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1a6e96f8-bd9f-3e07-8219-81ba0188b188 | -18.47982 | -53.40153 | 2025-11-11 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ca540c7c-19dd-3cae-bf92-3fb40c5b39fe | -18.47234 | -53.40884 | 2025-11-11 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0bf4ca48-b4aa-3efa-b3ae-08dfa5be7404 | -20.74247 | -49.7748 | 2025-11-11 04:04:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5f680f05-b066-340e-a97e-898d7a1cb97e | -18.38963 | -54.99574 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 8f3e9d6c-f234-388c-934a-e56703212720 | -18.1909 | -46.92533 | 2025-11-11 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb8a6a42-4cef-39ca-af01-94e19118829a | -18.39325 | -54.98978 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 89b8f980-80bf-3098-ab49-63e303871f47 | -18.03028 | -46.77986 | 2025-11-11 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e67405bf-25b5-3315-93e6-6ee5230dad19 | -21.32195 | -49.51323 | 2025-11-11 04:04:00 | NOAA-20 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 805b172c-84fc-3d45-a5fb-a2e47d3a056d | -18.90125 | -46.44961 | 2025-11-11 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55f16bb0-585f-3e1a-9d61-092aa53fd268 | -19.73753 | -58.06805 | 2025-11-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9787c4f6-5dfe-33d2-a8d4-519a686e5bcc | -21.42092 | -47.67501 | 2025-11-11 04:04:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cfa5503d-7e0e-3978-b619-6401dc865a5e | -18.18241 | -46.92899 | 2025-11-11 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d269dac7-cace-3f9b-85a7-5e6d1fcf2c6d | -19.31306 | -50.50207 | 2025-11-11 04:04:00 | NOAA-20 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e118770c-fa5c-3225-a1de-203e298b8e00 | -21.42001 | -47.67994 | 2025-11-11 04:04:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b658d93e-cc54-338c-99cc-422193fe4645 | -18.18621 | -46.9296 | 2025-11-11 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30ceb771-1e30-3169-b92f-f75233354c58 | -21.58528 | -48.35032 | 2025-11-11 04:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8962b478-6398-35a8-a222-af1d82187545 | -19.74458 | -58.0701 | 2025-11-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 10e1b707-2ba4-3a9e-ae8d-226ba69b739a | -18.24505 | -51.27751 | 2025-11-11 04:04:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1f1238a-036e-38c4-bf66-e41cf5262fce | -18.38581 | -54.98398 | 2025-11-11 04:04:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e4e01ab-1b3e-3f7b-91e5-91aba9d14a72 | -18.90497 | -46.44778 | 2025-11-11 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5ed02ed-ef51-3465-81ed-92890a4b1933 | -18.03318 | -46.78545 | 2025-11-11 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d698a6f1-6564-394c-b972-abef8fe10647 | -20.60391 | -44.65894 | 2025-11-11 04:04:00 | NOAA-20 | CARMÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3114501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1f2ddc2b-2fc9-375d-be2e-b1bcb72a2459 | -17.80737 | -51.73782 | 2025-11-11 04:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fe6d450-9a67-3174-870a-4e799de68a54 | -17.80144 | -51.7405 | 2025-11-11 04:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa7d84dd-d662-3fdc-9291-3b92a85a8f55 | -18.38709 | -54.98821 | 2025-11-11 04:04:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16609fa6-486d-3c44-9e39-547c7bde7651 | -18.38846 | -55.00083 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2d0655c7-ca26-357f-911b-a6f94285612d | -18.47792 | -53.41034 | 2025-11-11 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a2c00e04-0f8b-329e-8536-48f550fb2b74 | -18.3908 | -54.99063 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ffbcea3-db2e-36b4-aba6-bfd135de8a27 | -18.47887 | -53.40593 | 2025-11-11 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 19f80ebd-bf49-33d2-acec-e61ed23e4537 | -18.39212 | -54.99488 | 2025-11-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cc5f75b2-59ce-33a3-a5fe-9c13ea83527b | -17.86936 | -45.54467 | 2025-11-11 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a103dbcc-b8fd-3def-a6ed-6f949b357416 | -16.69352 | -51.83407 | 2025-11-11 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09ef0cb7-45dc-3b22-bd4a-d7d95152a185 | -21.41627 | -47.67908 | 2025-11-11 04:04:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 056eeab8-6c80-370c-8df9-e6fca9a6154d | -20.59554 | -51.61298 | 2025-11-11 04:04:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
