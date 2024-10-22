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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b0cab3-305f-3587-9812-42eb007b5d3d | -3.16615 | -43.9394 | 2024-10-22 12:29:00 | TERRA_M-T | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3d7cef71-7d16-369d-9001-f12a68740d66 | -3.16483 | -43.94848 | 2024-10-22 12:29:00 | TERRA_M-T | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 5ad01b59-fad8-32e6-ae00-bb287def5fca | -3.15716 | -43.93813 | 2024-10-22 12:29:00 | TERRA_M-T | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| de314a6b-d374-3cda-9689-0fcfa6506998 | -3.15584 | -43.94721 | 2024-10-22 12:29:00 | TERRA_M-T | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 993211e7-0aee-32af-84fb-b8a25b39dfcf | -3.51375 | -44.02279 | 2024-10-22 12:29:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| ddffd8b1-cef6-3976-acab-e04daa46d96f | -3.31216 | -44.1402 | 2024-10-22 12:29:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3bcde38b-edeb-3812-bb1a-d429511d61b8 | -3.31083 | -44.14936 | 2024-10-22 12:29:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4534639e-fc4f-3323-bc8a-8914bd67e8e1 | -3.22126 | -44.38607 | 2024-10-22 12:29:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6e94b456-33c1-3a4a-b210-ec0b59583d68 | -3.21214 | -44.38477 | 2024-10-22 12:29:00 | TERRA_M-T | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ceedf926-074f-38c3-b3c7-da04b58cbdc1 | -3.62141 | -43.34429 | 2024-10-22 12:29:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9c67795a-241f-3be2-b4d9-9c386ea5aa14 | -3.26212 | -43.27799 | 2024-10-22 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 361ccb9d-25a3-348b-9214-997d2952ced5 | -3.17383 | -43.25046 | 2024-10-22 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a1363921-b912-3081-a1e7-ec872b82ef7d | -3.17255 | -43.2593 | 2024-10-22 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e2689543-e487-324c-ac7c-93950e6b4192 | -4.4082 | -43.96273 | 2024-10-22 12:29:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f8c7e197-5600-3c3d-947d-c4c74b8f92f8 | -4.99766 | -44.47006 | 2024-10-22 12:29:00 | TERRA_M-T | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 28b9ff90-9e68-363d-a8c5-07a35419e410 | -4.17698 | -44.34385 | 2024-10-22 12:29:00 | TERRA_M-T | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 77a74ef8-9a7e-30cb-81e7-4542a5d707ca | -3.62353 | -44.40738 | 2024-10-22 12:29:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9a0bce5c-09e6-3edc-a846-6de4b016e236 | -4.82568 | -43.24343 | 2024-10-22 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b71b8ed7-5a1c-33d8-87c0-2c6fa95071dd | -4.81682 | -43.24218 | 2024-10-22 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 80b1c7cb-2df8-3d9b-bf49-9d6e8afc05e2 | -4.81554 | -43.25101 | 2024-10-22 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9e9e8e86-e85c-3945-87e4-252e839c9431 | -4.66041 | -43.81 | 2024-10-22 12:29:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 9416518c-118f-3822-8be5-f82e1f2efa7a | -4.40171 | -43.31204 | 2024-10-22 12:29:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2481fc1a-5ffd-340a-b87a-0a2e622eb475 | -4.39995 | -43.57338 | 2024-10-22 12:29:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9f726e55-34fb-3b57-ba85-3626762f26c2 | -4.34401 | -43.26142 | 2024-10-22 12:29:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4db96885-5099-3276-a4b2-0ffda3cd658d | -4.28345 | -43.74081 | 2024-10-22 12:29:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7c6092d7-582a-34fd-a188-0da7dd2d9d61 | -4.15565 | -43.73506 | 2024-10-22 12:29:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a2f93c1d-fbbc-3681-bc50-bc1ebaabd19e | -4.15435 | -43.74398 | 2024-10-22 12:29:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0ecd9087-f292-36e1-af86-44d2f2f12d66 | -4.1477 | -43.71827 | 2024-10-22 12:29:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bf7614c2-cb48-3748-803e-1663de7d0a11 | -4.14641 | -43.72718 | 2024-10-22 12:29:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 692829ac-dae7-3e35-9fef-1a813648e2f3 | -3.89144 | -43.13997 | 2024-10-22 12:29:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7fbb90fd-d913-3297-87ef-afe772524bd8 | -3.74315 | -43.46421 | 2024-10-22 12:29:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4df608d4-11b7-353c-b712-daebae625c11 | -6.40039 | -43.83024 | 2024-10-22 12:29:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 94bcf2f2-677e-3ed6-84c4-c3bb50df3a74 | -5.861 | -43.73472 | 2024-10-22 12:29:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5d03edaa-9014-394f-9a76-e11f96e421f9 | -5.85972 | -43.74357 | 2024-10-22 12:29:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 227ae77f-9aaa-3000-85dc-7e50edee4f89 | -6.24537 | -44.13769 | 2024-10-22 12:29:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b0b7d479-c547-30dc-9755-9e91d542490e | -6.24407 | -44.14662 | 2024-10-22 12:29:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f91270c7-f929-3d6d-b3c6-5e4e44d38589 | -6.13604 | -44.69482 | 2024-10-22 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bfe10998-a5eb-3c74-ad39-3cd6c22172d3 | -6.12123 | -44.91956 | 2024-10-22 12:29:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| ddd0d1d4-f20e-30db-8a2e-6341694290b9 | -6.07269 | -44.6234 | 2024-10-22 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bb44bc41-0a5d-3057-b9ca-6f716bcdd510 | -6.07133 | -44.63259 | 2024-10-22 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 377bbbe1-ae6b-3467-a6b9-a96bee26272d | -5.9515 | -44.88252 | 2024-10-22 12:29:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e1837eff-c064-3e8b-a3bd-81bf91474a85 | -5.24494 | -43.59477 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| aea1cae9-edee-3569-8c51-94097417d391 | -5.24365 | -43.60362 | 2024-10-22 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 61d24260-d609-3451-a1c3-a337416bd463 | -5.20419 | -43.68844 | 2024-10-22 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7782650e-8102-3985-a16d-47524fb226e1 | -5.62778 | -44.38895 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0fad8a6c-584c-3ff3-af05-a5998b4b990c | -5.62644 | -44.39803 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fd0fc37-f2df-375b-9578-987985924d45 | -5.5919 | -44.88247 | 2024-10-22 12:29:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 384202a5-863e-3f2b-b445-9820fe34f0b2 | -5.59078 | -44.70169 | 2024-10-22 12:29:00 | TERRA_M-T | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0aa64189-e7e6-3518-b993-9b1e89695043 | -5.58418 | -44.87175 | 2024-10-22 12:29:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 4f7e3b68-2d3f-35b5-b33c-174e0c9b203b | -5.58279 | -44.88115 | 2024-10-22 12:29:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ccaebdb2-f211-3c1e-a123-0037c884ca49 | -5.14358 | -44.29182 | 2024-10-22 12:29:00 | TERRA_M-T | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4eee5dd2-83f9-3f2b-80c6-8187e011f3e9 | -7.83792 | -44.15273 | 2024-10-22 12:29:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1d8d576d-8b71-3430-8c41-9142e0079339 | -7.83663 | -44.16162 | 2024-10-22 12:29:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9249b5c3-4d3c-39b3-8d04-4b7ab48d5c14 | -7.82906 | -44.15146 | 2024-10-22 12:29:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7d93b809-4d79-3f9b-a8ed-a91ca1cd541f | -7.82777 | -44.16035 | 2024-10-22 12:29:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 46abd87f-a051-3efc-b824-b06a09ccac84 | -7.13035 | -43.82086 | 2024-10-22 12:29:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 80104d58-f0e7-306c-8424-ade495329f51 | -6.93181 | -44.04295 | 2024-10-22 12:29:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea8bfdae-c405-3f79-b51b-f30cdb19952c | -6.93052 | -44.05184 | 2024-10-22 12:29:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0d289ca8-13da-318d-9bd0-a7b31509c002 | -6.83675 | -43.75135 | 2024-10-22 12:29:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| acfa532c-c92d-39b4-a1af-346d5c9e1ae3 | -6.69531 | -43.95415 | 2024-10-22 12:29:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b4357401-891f-3018-81b9-2645dd64d7a2 | -6.69402 | -43.96303 | 2024-10-22 12:29:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e896ad83-e312-3b30-87d7-81ca9d47cda9 | -7.19513 | -44.76634 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 0490bc39-c718-3c3d-a7f3-5def7443e8aa | -7.1938 | -44.77547 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 317d0cd5-c2cf-3b66-987c-704173b7a3e1 | -7.03291 | -44.48986 | 2024-10-22 12:29:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ffa30f13-508f-3430-84a9-55b88fc2a707 | -6.97142 | -44.5298 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8bdc5bd1-e255-3a23-94ad-59069e37d106 | -6.97011 | -44.53878 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| df0f2676-4395-3bb8-81c9-cc45d2a99dbe | -6.96248 | -44.52851 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1a15c3c9-a365-30aa-bdfc-9838fcc83b3b | -6.94558 | -45.20951 | 2024-10-22 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c941dc67-743e-32a5-99a8-659986ef72e8 | -6.55737 | -44.01916 | 2024-10-22 12:29:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5754f35d-1db9-32a9-8d10-36d7b565e03c | -8.61618 | -45.13745 | 2024-10-22 12:29:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 48bb8005-4c20-365b-87f4-7f21ef4aaa63 | -10.44999 | -44.89921 | 2024-10-22 12:29:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ffa6378a-e65c-3c97-95ec-a31fc3a8633d | -4.8978 | -45.83373 | 2024-10-22 12:29:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 029a9560-a2cc-367f-9c73-784189d92843 | -4.36544 | -44.69668 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2b88bd4b-e916-3ebc-a7ad-7d6e54502ce8 | -4.36407 | -44.70609 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9e525a83-721a-3c54-8922-3cda50476534 | -3.97147 | -44.74125 | 2024-10-22 12:29:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 029554a3-2f5f-3969-86c3-7ea8dd4da623 | -3.97008 | -44.75077 | 2024-10-22 12:29:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 57cef8df-c211-3d90-b81c-8c10ac043299 | -3.90401 | -44.57125 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 30a4a835-5079-3c21-b077-d8fe9d77b759 | -3.90264 | -44.58065 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4969e8af-36c4-3e9c-86f6-cd2e2ba252a2 | -5.69606 | -45.49001 | 2024-10-22 12:29:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9d566265-243a-3014-81bd-d10f93c8aede | -5.2716 | -44.86908 | 2024-10-22 12:29:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 50e88867-cc68-34fe-9b19-c4943363252f | -6.9442 | -45.21894 | 2024-10-22 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 18554d40-6882-38df-8d30-f3445fbd12d5 | -11.96385 | -39.54221 | 2024-10-22 12:32:00 | TERRA_M-T | PÉ DE SERRA | BAHIA | Brasil | 2924058 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 7459cd22-ac6b-3c0e-84bb-3abb356ecec9 | -11.99691 | -43.08599 | 2024-10-22 12:32:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 1e6e078a-af67-3b48-9c13-f6b7c7f04e6d | -13.44655 | -43.17685 | 2024-10-22 12:32:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d096cb83-ad95-3f44-86a2-cf71511fc91f | -13.4452 | -43.18689 | 2024-10-22 12:32:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3949823b-87b8-3fc7-a7a2-1c61a3bf1fa3 | -12.91847 | -42.31227 | 2024-10-22 12:32:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 51d028d1-0292-3164-84aa-b9575d96eab6 | -12.79698 | -42.35991 | 2024-10-22 12:32:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 3b045c0b-b805-34e0-9e7c-a93f79b192e7 | -12.78737 | -42.35863 | 2024-10-22 12:32:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 852897d6-fc31-376a-841f-dcc3133eb227 | -12.55848 | -42.47651 | 2024-10-22 12:32:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ea4ff6f7-8044-3523-aff8-5ba67aad7fec | -13.10013 | -43.36409 | 2024-10-22 12:32:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e5634081-a9a9-3cd0-b5fb-706a88ef29f0 | -15.07499 | -43.11337 | 2024-10-22 12:32:00 | TERRA_M-T | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 2e0dd3f7-e234-39e1-bad8-8c695e2c5e87 | -13.97401 | -42.81236 | 2024-10-22 12:32:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 28.0 |
| a30a2fab-d342-3c6f-bb1f-f945ecb04a1c | -15.22868 | -43.33669 | 2024-10-22 12:32:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 06144a97-fa8b-385b-87e4-75dd1ced9e78 | -12.02971 | -44.17116 | 2024-10-22 12:32:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6d863828-9537-3d51-8e83-8f74005a20e8 | -11.90938 | -44.16914 | 2024-10-22 12:32:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3b9c5918-ab06-35ae-99c8-9b9edb3f96e0 | -11.90808 | -44.17822 | 2024-10-22 12:32:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9f824d7a-d96d-37fe-b996-8b577fe083b6 | -11.88215 | -43.38585 | 2024-10-22 12:32:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9b11db4c-faec-393e-90bb-217c4d301f84 | -11.82923 | -44.86323 | 2024-10-22 12:32:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 30f27fcf-20bc-3531-8452-2a3d5c3cac87 | -10.81589 | -47.61978 | 2024-10-22 12:32:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 87953c44-9944-3643-ba22-84ccd335bc82 | -18.30501 | -56.10489 | 2024-10-22 12:34:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.4 |


[Clique aqui para ver as próximas entradas](README35.md)
