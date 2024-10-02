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

## Dados Diários - Página 203

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a190abe-9f8c-3a48-a37e-002653df42bc | -6.83945 | -41.82415 | 2024-10-02 12:14:00 | TERRA_M-T | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0bf6ca35-511d-3b40-b1ff-1e170737146b | -6.84893 | -41.82556 | 2024-10-02 12:14:00 | TERRA_M-T | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 27f6b441-b2fd-35c5-8344-d92b6dc73c9c | -6.24643 | -41.86328 | 2024-10-02 12:14:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e212fca5-933c-3c3b-b79f-e549b92f37d2 | -6.24799 | -41.8528 | 2024-10-02 12:14:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| a3d7d250-9d6b-3c5c-a303-d7d0f877ca41 | -12.71486 | -40.44609 | 2024-10-02 12:14:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f936693a-b48a-3f49-b7c4-d7796e604a4e | -10.57942 | -40.04321 | 2024-10-02 12:14:00 | TERRA_M-T | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7be1447e-5d37-3122-a200-349987675dd2 | -8.82923 | -40.73209 | 2024-10-02 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| add17e08-56be-3f08-af03-db60646f964a | -9.1038 | -39.98739 | 2024-10-02 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| ab3c6c37-8f4d-34f8-b115-979567eb43b0 | -7.07793 | -39.14748 | 2024-10-02 12:14:00 | TERRA_M-T | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| aecab513-2fcd-3a98-8378-7e58ecda4fa1 | -6.46644 | -39.73891 | 2024-10-02 12:14:00 | TERRA_M-T | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 242e4cfa-5528-368d-bd7f-be08f924a2e9 | -3.98141 | -39.58242 | 2024-10-02 12:14:00 | TERRA_M-T | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 09cb0447-d33b-3317-9aa6-49efd162270f | -4.67361 | -38.624 | 2024-10-02 12:14:00 | TERRA_M-T | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 0375a330-136d-38d2-bd1c-25722f35863c | -12.57156 | -40.03212 | 2024-10-02 12:14:00 | TERRA_M-T | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6ff61f4a-13c8-3915-82e3-84ed16b16d42 | -12.04638 | -39.18299 | 2024-10-02 12:14:00 | TERRA_M-T | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 0fd56182-cb5e-36b3-be10-cc0ce7a2ef21 | -11.66071 | -39.96008 | 2024-10-02 12:14:00 | TERRA_M-T | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 02347b72-85db-38dd-a339-fc10fd37dfd2 | -7.158 | -44.22077 | 2024-10-02 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| dfa51a39-3357-3170-8dd7-6d522bab2781 | -7.08933 | -44.14367 | 2024-10-02 12:14:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| acd8b9b4-c22b-33a3-b875-13d1d98a7c64 | -6.88004 | -44.0859 | 2024-10-02 12:14:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7adbc532-1622-337d-9e1d-6deb958f9cee | -6.87783 | -44.10008 | 2024-10-02 12:14:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c4437b89-80fe-338d-aec2-711310ffb878 | -6.57089 | -44.83336 | 2024-10-02 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1d060a2a-70ec-3d22-8ced-163a6ca53452 | -9.01439 | -45.22498 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 12076831-cf84-3a67-afa7-ec15d1656076 | -9.00017 | -45.23909 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a353b34b-966f-3a37-bd21-5816730585df | -8.99762 | -45.25483 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 84c167a5-3ca6-377d-8f93-581ac748c25b | -8.99072 | -45.24681 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| fef73cc7-e0e1-34bb-ab58-2fb7b646daa2 | -8.98821 | -45.26301 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.2 |
| bc55e543-6012-3e88-83fc-1537ab649008 | -8.98597 | -45.25282 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4644fe3c-b206-3a9e-9c2b-1b8b8c61fedb | -8.98332 | -45.2691 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 955f2510-e3a5-388d-adad-6fee48e413b7 | -8.93506 | -45.64088 | 2024-10-02 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 13e26379-1e1d-3419-a0c1-7e6572eb36b0 | -8.69967 | -45.23969 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3836e901-7239-3058-be35-4728c3a74cc5 | -8.69294 | -45.23228 | 2024-10-02 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 08e55718-be08-34c8-b45b-dc72a971142d | -8.63449 | -44.06508 | 2024-10-02 12:14:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| be1b89aa-6083-3901-9cac-5314350fd422 | -8.20911 | -44.35383 | 2024-10-02 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 557e0f37-d52d-3ed3-bee4-756d1739e09c | -8.20682 | -44.36825 | 2024-10-02 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f8acff1c-7296-31dd-ade1-fa36801bc82a | -7.16699 | -44.23638 | 2024-10-02 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ebb731e0-f616-31ca-ae7c-f4cdce7b3d68 | -7.16916 | -44.22232 | 2024-10-02 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 54fb0746-cf97-384f-812b-8e62ac5cae71 | -7.27659 | -43.81033 | 2024-10-02 12:14:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cb1d1927-b6fb-3151-bfbd-e1e90fd12092 | -7.64685 | -43.96745 | 2024-10-02 12:14:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d28a716a-e659-3657-8bd2-995bdc8e6365 | -7.6556 | -43.98245 | 2024-10-02 12:14:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| f3c2249c-b6d9-3803-981f-f37c2039dfbe | -6.08156 | -44.71109 | 2024-10-02 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cc3f7fcf-0c6b-3557-9fa1-4ce76169d75a | -6.08411 | -44.69452 | 2024-10-02 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 254f63a2-5afd-397e-bd07-c0fe5eefa8cf | -6.09337 | -44.71281 | 2024-10-02 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 84f27244-a7e4-3e8f-b3fa-b04e205a74dc | -6.09592 | -44.69615 | 2024-10-02 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| fd472458-1551-31a2-b551-d3acc95d096b | -6.11282 | -44.94492 | 2024-10-02 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| f2d8c3f7-b097-3acc-91ea-9300765d04be | -6.11549 | -44.92791 | 2024-10-02 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b6e31b5d-10c5-3b5c-940d-15fe0af04d54 | -6.4995 | -44.08397 | 2024-10-02 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 02d187db-a33c-32de-9621-a9fcc25f7835 | -6.40297 | -43.81541 | 2024-10-02 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| ca9c8f22-73bd-3b2e-aab5-5847d3878c0a | -8.20603 | -44.36139 | 2024-10-02 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 5a925433-5f2a-30a6-a874-795ef9374e70 | -8.20384 | -44.37585 | 2024-10-02 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1ec3eaaf-f48b-38eb-9ba9-75c611dc7912 | -8.1981 | -44.35195 | 2024-10-02 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 43b77f44-74ca-3f75-bb5b-a6e6043affb6 | -8.19581 | -44.36627 | 2024-10-02 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ff7aef21-199a-3258-999a-99d31b08d0ec | -7.86868 | -45.32526 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 820e0c0b-7834-327b-bc63-9c15047ada86 | -7.86595 | -45.34211 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 24b36ee7-87f2-39dd-8799-27cb89d42d5f | -7.86138 | -45.33456 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 4c9b3876-ea14-3502-87ff-0f384d35ad0f | -7.85394 | -45.3402 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 39fb2f7e-4f28-36a9-8301-7e5aa0656579 | -10.79196 | -45.55618 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 48e7af5f-155d-3806-abb8-8d7fedb2ff8a | -10.66473 | -44.49894 | 2024-10-02 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 375806c8-6208-37b7-bfe5-dd633be1383f | -10.66119 | -44.49234 | 2024-10-02 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a6e1f828-9609-3f25-9211-cd9a69bd26d8 | -10.88336 | -45.97182 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| c4f27b83-07ed-3952-b11e-7d68071df39c | -10.87846 | -45.96404 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| d8e7b43c-af28-374c-b623-9bd1ba13b674 | -10.87572 | -45.98111 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 9d1f24ab-7a89-3d60-a45b-eb1f614f9176 | -10.80351 | -45.5582 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 62c0627a-cb76-36ec-9651-d779b1501f74 | -7.7172 | -45.43088 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| d7aecb6f-bc95-3e5f-82ac-8fc3df16b736 | -6.97775 | -45.37369 | 2024-10-02 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1d5aa96d-c465-3592-9226-4d981945d3e3 | -6.96836 | -45.3538 | 2024-10-02 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 5b44e7c9-174d-3ad6-927a-12bc8a8fe9a3 | -6.96551 | -45.37177 | 2024-10-02 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| d65f7a5b-4368-3f03-9bbc-79b135923eb2 | -8.93224 | -45.65818 | 2024-10-02 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| da6d10a9-5dbd-351c-91e4-1aa4af8a3fce | -8.92816 | -45.65089 | 2024-10-02 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| dcc7b8c7-f95f-3a1a-93ad-c5aa6c8dd8e0 | -8.44432 | -46.31259 | 2024-10-02 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 3cccfe2c-07c6-3a5c-be78-3aed72abfe33 | -8.44286 | -46.31925 | 2024-10-02 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 35702c4d-8add-3951-b693-8be7711360d3 | -8.43151 | -46.31019 | 2024-10-02 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9b660e59-1d4c-347d-ba15-37ad8de8e75f | -8.42015 | -46.37642 | 2024-10-02 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 9e8f2125-ce75-3859-9d76-e813eedd14c1 | -10.72585 | -46.18425 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 421e30a1-6e39-37f5-8ba2-6abfad2fcdb0 | -10.71662 | -46.16423 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d1ef0597-0d37-32d6-9719-a9d23f50752b | -10.71379 | -46.1815 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 1fb3fd0e-7029-3cac-b513-5fda51eb0340 | -10.68599 | -46.12309 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c78ffe9e-639e-3025-964d-295d87028d4d | -10.68236 | -46.11576 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e38a9aec-cb1a-37b3-8b59-562e1d07ea60 | -10.67959 | -46.13314 | 2024-10-02 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| f084fcbd-187a-37d8-a276-0c23e4ff3bf9 | -10.50958 | -46.30318 | 2024-10-02 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7d57e368-8301-31db-bbf5-0da668e8fa9d | -10.49722 | -46.30119 | 2024-10-02 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 8c54d1cd-a4da-31e3-92c0-f6f2b9a37caa | -11.3039 | -46.8324 | 2024-10-02 12:14:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| eced3571-780f-3a45-8f3b-ab8b11af21d8 | -11.30099 | -46.84522 | 2024-10-02 12:14:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 300de1ba-dbd9-3adb-bb4d-11eec72abe01 | -11.29718 | -46.87187 | 2024-10-02 12:14:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 45958b24-74d8-3f1c-af35-ae5971ba5edb | -11.29452 | -46.88503 | 2024-10-02 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| bea878a4-91ce-3984-a81d-3c17c44676f5 | -11.29378 | -46.89177 | 2024-10-02 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5cd9713e-7b2a-3548-b880-8e2df72295de | -11.0258 | -46.5239 | 2024-10-02 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 798f7982-9c47-3d7b-9690-d5e3e2d08e60 | -11.01657 | -46.50251 | 2024-10-02 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a4aeec89-02e4-3195-a834-941f6d8496ac | -10.9966 | -46.45208 | 2024-10-02 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| da9eda0c-30a4-3ecd-9c83-71c5269a20bb | -10.73223 | -47.64526 | 2024-10-02 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4b9fe9d6-1028-35e3-bbd5-d8dcc770f49b | -10.72576 | -47.63828 | 2024-10-02 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 5fa3ce52-d257-3713-a134-a5c99e76db96 | -10.72199 | -47.66138 | 2024-10-02 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 1e8d5fb2-2c59-369c-9e57-d72307f8c396 | -10.71857 | -47.64281 | 2024-10-02 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 245.4 |
| e121f87b-f437-3dfe-bc82-f81eb8247120 | -10.71464 | -47.66574 | 2024-10-02 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 765d7fa4-c2b2-38ab-bb74-23c7d88566d2 | -10.5984 | -48.06018 | 2024-10-02 12:14:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1b1a85be-c127-36fc-ab6a-07324d78dbd3 | -10.58428 | -48.05741 | 2024-10-02 12:14:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 8078fb03-b6ad-33a8-824a-274574c475d2 | -10.56031 | -48.0273 | 2024-10-02 12:14:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ab059356-357b-3223-86fd-a906baa383e9 | -10.55717 | -48.01982 | 2024-10-02 12:14:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| b6111405-d117-367b-8b3f-bfe4f4b634d8 | -6.79078 | -38.51393 | 2024-10-02 12:14:00 | TERRA_M-T | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| fa901668-48fe-34cd-9a27-4852287aaf17 | -7.47271 | -38.38143 | 2024-10-02 12:14:00 | TERRA_M-T | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 19.8 |
| fce55773-4fad-3a88-889f-0774eb15547a | -7.77817 | -37.20573 | 2024-10-02 12:14:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d01b779b-9a12-333c-b743-5e8eb340377c | -7.75772 | -37.66403 | 2024-10-02 12:14:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README204.md)
