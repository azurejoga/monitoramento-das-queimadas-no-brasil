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
| 5a3f8381-ff52-34db-a31f-623e13205eb1 | -6.55404 | -60.02797 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 030812dc-9734-383b-ba8e-ba6cd310077c | -6.55348 | -60.0315 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7a08dd7-c466-343d-a409-459ea30a5d73 | -6.55293 | -60.03503 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e237335b-ee4f-36ca-a10b-03eaeba2d2ca | -6.55127 | -60.02391 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5507a14-8440-3ac7-9317-979313162ab5 | -6.55071 | -60.02743 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d64f596-67dc-32b1-a32c-7f375fb26962 | -6.55015 | -60.03096 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d3bdbc3-bfe1-3286-8a68-8bb3e8df3596 | -6.5496 | -60.03449 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 520dd3ba-620e-372c-aebb-e188c75063e0 | -6.5485 | -60.01986 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5bd83a0-1dfd-3313-b753-2dd2ca3d7fb3 | -6.54794 | -60.02338 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 436b32e8-bf60-30fd-bbac-2fb5a9131684 | -6.54738 | -60.0269 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eedad17f-804b-318d-88f3-ad507436a0be | -6.54682 | -60.03042 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d7dd7a1-e9b1-3e74-a62d-8fbb9507029d | -6.54516 | -60.01933 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 176749d3-2f93-3eda-8a4b-c18dce7424ea | -6.54414 | -59.76768 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce41cf5d-53b8-3cf4-8329-74efe9549ffe | -6.54405 | -60.02637 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ee5ee18-838c-3488-a4c2-f8d4cd5c2d55 | -6.54349 | -60.0299 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 953d56b3-e752-3315-8296-952edb1ef918 | -6.54239 | -60.01529 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2cf8127-e266-3c6e-a70b-61b3ba461d3a | -6.54137 | -59.76368 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c0aa148-d701-36fc-addb-c934bbed260a | -6.54082 | -59.76717 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e98172a3-e793-3360-8dd5-bd56faae14ce | -6.53961 | -60.01125 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beebf369-3e94-3d5b-9848-5aeec348e250 | -6.53906 | -60.01477 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30144dc9-77bb-3815-8af7-d8a6a37f951a | -6.5318 | -60.06057 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 833d3109-425e-396e-8322-300c54dbadf9 | -6.52847 | -60.06004 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82760aa9-04bd-3f84-873f-2593c7fd139c | -6.5257 | -60.05598 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df3cd55-df4c-34d3-b213-b31ad739bc85 | -6.52514 | -60.05951 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f9fc897-0d03-3d34-afc6-47275c66d31f | -6.52236 | -60.05545 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c09f2db-4b28-3db7-9491-ba9db52d486b | -6.5218 | -60.059 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd212291-6729-3737-9542-42518c5bf71f | -6.52124 | -60.06255 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43cd4367-e0a3-3720-9605-29a5bbc8f902 | -6.51903 | -60.05494 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bb6f70d-8905-3009-944a-049d36adf796 | -6.51846 | -60.05848 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0dba79a-028c-38be-96d8-0b590695a5f1 | -6.5179 | -60.06203 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9d35e8f-71eb-3de5-8a00-ae9b8c5d1132 | -6.51513 | -60.05796 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 105829cb-ce6f-36f0-916a-37202f3258b0 | -6.51457 | -60.0615 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6eed8dfb-a4c1-3da4-a2d8-16361a9cb904 | -6.49747 | -59.97571 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b405d12-e549-333d-be9a-9561cd20816f | -7.14188 | -59.30206 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14f9b0a2-dd36-36ca-8599-33a74d727df2 | -7.14134 | -59.30551 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 346db931-4b77-31e5-955d-20e636fb9700 | -7.13804 | -59.30499 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c591f017-d8b5-3924-a167-53f30953894d | -7.13654 | -59.37901 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68680af3-6b9c-303c-b1c7-4b893dcfe046 | -7.13323 | -59.37849 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51399048-7a30-3069-8619-c2b101e5aa95 | -7.13074 | -59.22247 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3d4760c-c9f0-3b15-a46f-a990e0f60109 | -7.12694 | -59.24664 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4260e75d-4b13-3257-8d9b-f278acc6799c | -7.12522 | -59.21453 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30b9a676-b9ac-3591-b141-8c086df3cdf4 | -7.11867 | -59.23473 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4ed09bc-c8b2-32b2-b8d4-29a4fb259276 | -7.11812 | -59.23817 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b28c96a-a04d-32b3-a83b-b4410f80cf50 | -7.11799 | -59.21331 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca3ac352-a497-3716-8728-09706b32dc06 | -7.11636 | -59.22367 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c25541a-2632-3e69-be38-a7c8b920a1c3 | -7.10552 | -59.29271 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d482b25e-1de1-3b05-8e72-4820a330c22e | -7.10497 | -59.29617 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 319fd2ba-7e12-3a7c-8f26-a8191c700ff8 | -7.10443 | -59.29962 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02900824-d28c-3b5d-8534-8ff884e6c6e3 | -7.10222 | -59.29219 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c95badd1-9d60-33b8-98bd-667ec3314b28 | -7.10168 | -59.29565 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69ddef29-3663-35ce-a40c-ad94c4897850 | -7.10113 | -59.2991 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8060cee-3d3d-38cb-ab20-73037e0e5bbf | -7.09892 | -59.29167 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c43d0b-eb98-3d3f-93ee-f92b13295bde | -7.09838 | -59.29513 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50ea184a-b908-37eb-952b-65aac24dda00 | -7.08731 | -59.258 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61e600bf-b1b0-3a9e-b4db-59a420c1281a | -7.08676 | -59.26145 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7321e39b-bfd5-3f29-8401-46835f69e6a4 | -7.08401 | -59.25748 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c31c314-2cde-3c1e-8f88-cb01cc215485 | -7.08346 | -59.26093 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dff74065-3acf-397e-b80e-35a1182030c4 | -7.08292 | -59.26439 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea888f86-1a26-3b6f-80e7-d5383b9531d9 | -7.07962 | -59.26386 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7c375b6-1ee7-3ce6-857a-c120dcd57591 | -7.07908 | -59.26732 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34405669-2bf5-3a3f-8907-6995069c5de3 | -7.07632 | -59.26334 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 151cea56-3cdc-3c1a-95dc-4d685d67dcaf | -7.07578 | -59.2668 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 000e42a6-1b32-34ec-970c-078da213de68 | -7.07524 | -59.27026 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 013c0e76-8245-3415-a039-0ebcc7f38333 | -7.07302 | -59.26283 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 399b7fd8-89bb-3f98-a971-bcf4f05349d4 | -7.07248 | -59.26628 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 516d639d-49c9-3bfb-95be-a723ceeda143 | -7.06972 | -59.26231 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f98faab8-00e1-345a-9c2c-7eb88e58c924 | -7.06918 | -59.26576 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dc48c0f-783c-3f56-9212-13f0e1b6c93f | -7.05342 | -59.36593 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b4e833c-e6d7-375e-92d8-f42e99df594f | -7.05288 | -59.36938 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eef56c7f-e246-3676-aba1-871fbb86f7fd | -7.05012 | -59.36541 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f0390f2-e9de-3bbb-bdac-64720e124b7a | -7.04957 | -59.36886 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6dd0cdf-6c7e-38ab-affb-51f9f38dddb2 | -7.04682 | -59.36488 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb0039c8-ec89-344e-8609-527abce1560c | -7.04627 | -59.36834 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ddda2c2-f656-3ce0-9c8b-e398cf330ea9 | -7.04352 | -59.36436 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9185978c-b5ef-3095-ac32-835a8e4ffbcb | -7.04297 | -59.36782 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aca2ee5-149c-3cef-a5b9-a75960790005 | -7.04022 | -59.36385 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd6ab48c-4466-3b3b-8b13-f97ee5b8891c | -7.03967 | -59.3673 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38b03257-31c4-32fa-9e98-0a34524f7f57 | -7.03914 | -59.3707 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbdded36-1057-3a67-b431-ff9c07ca70a1 | -7.03637 | -59.36678 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b888d350-7d98-3375-908a-a3233d0bd304 | -7.03584 | -59.37017 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20567086-738c-353f-a811-3ffcc22e1ab4 | -7.03307 | -59.36626 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 84d5b27e-51e4-3915-a49f-4b3a2b145fd2 | -7.03254 | -59.36966 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3ad209c-f8d2-347a-9484-aea62333e054 | -7.02979 | -59.36568 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8fc25df7-5833-3b28-b9d3-9891ea9618e2 | -7.01659 | -59.36361 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd1249ac-f8c6-3c28-80e8-8d9cf359f001 | -7.35186 | -59.93324 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba46ab9f-f21e-3956-a9a1-ffcef2a84027 | -7.3386 | -59.93112 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 147f3c1c-8fb4-3a6b-a55e-bf35031d5558 | -7.29693 | -59.74245 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbb24a28-dc90-3bb3-94d3-b9c2281ccfb7 | -7.27928 | -59.74679 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca064bc-a933-361c-bd7a-8cd423f29d91 | -7.21956 | -59.75797 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 870370fb-da6e-3140-a6e8-a0b83d41f6a6 | -7.18757 | -59.76717 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb3adf36-1e26-3417-a701-575288bf316f | -7.18426 | -59.76665 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a13affe-5c8a-3256-8643-cb7ce632d12d | -7.15415 | -59.39597 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce4bde2d-6df0-377c-a796-6348bc4577db | -7.15361 | -59.39942 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 648356be-c4b9-3f81-8b5b-33fd0555de6b | -7.11821 | -59.77405 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42076b11-e242-3564-955f-0a2215451908 | -7.09423 | -59.41132 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8afd23ed-2185-33ba-82c6-0b59789db532 | -7.09148 | -59.40734 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ebfc12-2737-34dc-adfe-b0849b2f382b | -7.09093 | -59.4108 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1a3c576-9dda-3f7d-acb6-f03b78b940aa | -7.0876 | -59.40664 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c029f1b1-e4c5-3c0b-b511-cfeea2ddd9cf | -7.08705 | -59.4101 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc6c6524-8e1a-348b-830f-8c2afc27aaea | -7.0843 | -59.40612 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README86.md)
