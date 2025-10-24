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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbd75f82-cc49-3151-941f-cd60cbf7fb56 | -2.44108 | -49.37279 | 2025-10-24 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a968664a-1193-3682-a756-5b0f2be2113c | -2.26446 | -47.8469 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de46d6d3-ae25-323f-b116-fb57b69b19fc | -1.92346 | -52.14014 | 2025-10-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccda9627-3bc2-3a24-a254-eab4389ddd21 | -2.39208 | -48.11382 | 2025-10-24 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7554d2a1-f5b5-30a1-9235-52b2b652ce99 | -3.70439 | -40.42588 | 2025-10-24 04:36:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 350fa54b-bb4d-3f8c-b18c-99941ce92d1a | -0.76287 | -48.55473 | 2025-10-24 04:36:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48826955-e95d-3e24-9737-9d7cdabab371 | -2.26115 | -47.84639 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e9abfe6d-988e-3c56-a38b-aa525ef8600e | -2.92278 | -47.80825 | 2025-10-24 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ee1b776-d484-3284-9277-7afe16d512be | -2.86884 | -41.74562 | 2025-10-24 04:36:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 955abe57-0300-3acd-822f-9f742cc43db0 | -0.57632 | -50.44239 | 2025-10-24 04:36:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70f07c76-7110-37b2-b76e-813263cd79df | -2.47107 | -49.22734 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c11a7c71-155f-301e-bf7c-2e419d7ada1b | 0.46922 | -51.0127 | 2025-10-24 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22123f94-b321-34b9-a490-33d145777937 | -2.77077 | -48.59902 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9981aa4c-e28f-39bd-935d-a6e623d427f0 | -2.73962 | -48.68917 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e16d0e42-535f-3057-b84a-10b06f9098fd | -2.29968 | -48.57067 | 2025-10-24 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99d1ca16-3f47-31ac-8d67-42746a5e2286 | 0.3631 | -50.93433 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a44a440-3518-3e4e-9b9e-a08b2df6a75c | -2.02797 | -52.11836 | 2025-10-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a7943a6-3f35-3f7e-b7ec-560fc1796b3e | -0.62089 | -47.66684 | 2025-10-24 04:36:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de9f029c-0c3f-346f-b51b-4270701011d6 | 1.57076 | -56.01321 | 2025-10-24 04:36:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2557479b-4d0f-32ad-82ce-b83f54a35228 | 0.10656 | -51.37305 | 2025-10-24 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ec3c5b2-924d-3aa2-946f-685123ba53a9 | -2.86813 | -41.75019 | 2025-10-24 04:36:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d155eb0-ee99-3d7d-b762-fd1802aee8d9 | 3.10996 | -51.43692 | 2025-10-24 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7249b789-4ce9-3bcf-aee0-e638dfe2c8a6 | -2.26169 | -47.84294 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 205a9ee9-725b-3b32-8259-f8decfb3c0e7 | 1.57029 | -56.01016 | 2025-10-24 04:36:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90a30faa-e2a3-3b96-b942-5cf64cad2f98 | -2.86514 | -41.74627 | 2025-10-24 04:36:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4c161fc-022e-3484-9f4b-c96adbb1bcfe | -2.47439 | -49.22786 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b69d9b46-17d2-399b-8b7b-474e93fd4d6a | -3.4177 | -44.81789 | 2025-10-24 04:36:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eacc28e0-4a2b-3e10-9026-344ed40dbc1a | -2.26669 | -47.85432 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4ca4d01-f25a-3ae7-a645-2ce86da658ef | -2.42649 | -49.27352 | 2025-10-24 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7a5a1aa-a07a-3c8c-afae-026b65d7deed | 2.71892 | -51.5596 | 2025-10-24 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf384f64-2b53-3b76-a913-ad80dd31dd6a | -0.86058 | -48.73252 | 2025-10-24 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa141f1-0e1f-3b63-87bc-9d83c0b3ef46 | -0.32949 | -48.69527 | 2025-10-24 04:36:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dba6d6d1-681a-3557-a59c-187f007a475b | -1.10226 | -48.8593 | 2025-10-24 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcc28fd1-ea2a-30b7-b056-796f734170d8 | 1.64894 | -55.75266 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffd3b6e5-d98d-3303-b42d-51c4cd218fee | 0.46559 | -51.01328 | 2025-10-24 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 389616fa-c0ac-3969-afdf-392035d6ebe8 | 0.40676 | -50.95304 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3285ccca-fd18-363d-a843-93ef1b09b2bc | -2.74016 | -48.68574 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a2d1c26-7155-3c79-9037-20c9e5db3375 | -1.55006 | -55.40969 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58bb9f65-6ec0-3c35-a557-6236f5c02512 | -2.69232 | -48.70995 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 897dcd55-dc83-36b7-a23c-39e841758b81 | 0.10955 | -51.36814 | 2025-10-24 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4174848d-392b-3b67-a933-b00121521c8a | -1.54538 | -55.40891 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1634ef2-5abd-3533-b7a2-e5be36ed6db3 | -3.29802 | -43.50015 | 2025-10-24 04:36:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b8b03c3-0fb7-3646-abdf-c99bb877f4d9 | -2.7462 | -47.13717 | 2025-10-24 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 223622f5-7763-3ae5-b6f4-f643f073692e | 1.66824 | -55.71087 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea850d8a-f2fc-336d-8530-07c845d1b573 | -0.1649 | -50.40895 | 2025-10-24 04:36:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dbb209e-5697-310b-b068-1d9480632be1 | -2.77023 | -48.60245 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1a23d7f-78d7-3f9b-97db-e747635ca857 | -2.77466 | -48.66337 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1548750-cdb4-34aa-8e9c-bee7204385a8 | -1.92273 | -52.14468 | 2025-10-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69d3bfa9-f8ab-3ac7-842b-bed07b83c0fd | -2.79274 | -48.89171 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3a0c744-216c-35d7-b971-361520f04fd0 | -2.25257 | -47.01768 | 2025-10-24 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acf9562f-a8f0-3cba-bde2-1acbeee17a12 | -2.68901 | -48.70943 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd6c8461-ca89-30b3-a90a-038c02be999d | -2.47661 | -49.23534 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf0812a2-25da-3926-acc0-be2ebacbb8e1 | -3.29856 | -43.4966 | 2025-10-24 04:36:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f117e94-4f92-3a7e-8a0b-eb0f6ad14f1e | -2.87208 | -45.25515 | 2025-10-24 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fdd1ebc3-7b6f-3247-87d0-e5fd46a165b8 | 1.35616 | -50.91707 | 2025-10-24 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36ee4ff2-a237-36ce-8ecf-b4dfc3f40297 | -2.26061 | -47.84984 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 59e66e6d-56a6-3206-85df-906f82412df1 | 1.55959 | -56.00869 | 2025-10-24 04:36:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfcd6a05-e59a-3a6d-b819-6883cd04643a | -2.47495 | -49.22438 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8beb5f3-2b83-3efe-8b03-1f9f7037b44c | -2.41546 | -48.44093 | 2025-10-24 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8da1e25d-7656-31f8-9920-68019f440cb9 | -3.32193 | -44.18325 | 2025-10-24 04:36:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1af6b783-2b6a-3bf7-866a-37153d402819 | 2.07342 | -55.7151 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39cf9212-eab0-3272-8b11-6a2f8e52839a | -3.7039 | -40.42386 | 2025-10-24 04:36:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b2e13cf8-bc9c-3243-8bab-8564ccf15697 | 0.4061 | -50.94888 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16273131-6b3d-3726-97d4-f148523731c6 | -2.86968 | -41.74695 | 2025-10-24 04:36:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a97ce67-49f6-38cb-ac33-3168ce421429 | 1.5647 | -56.00785 | 2025-10-24 04:36:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b29f8e2c-eea6-3c3b-8b03-41a2c5b6b304 | -2.79835 | -48.94202 | 2025-10-24 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abf7e94b-7df3-395d-9265-1e9f240dd280 | -2.25201 | -47.02125 | 2025-10-24 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad4ad75c-f6c7-3570-830d-c1f09a33e1ca | -3.70347 | -40.42682 | 2025-10-24 04:36:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e464f1dc-994f-310c-afd1-34dd5b84ce8f | -2.26392 | -47.85036 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8db8a363-2a26-3b59-a9c3-0f5267cfe582 | 0.36606 | -50.92962 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a258291-5887-3865-af17-3acf3a772ce3 | -3.32396 | -44.27237 | 2025-10-24 04:36:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 384f6672-bd09-3b45-9639-67d9900b5946 | -2.4923 | -48.1469 | 2025-10-24 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 683567de-fc88-34e7-9263-439e4e89a4bd | -2.44408 | -47.16003 | 2025-10-24 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 725c675e-e897-3042-a369-4be5e21f75ea | -2.26723 | -47.85087 | 2025-10-24 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d649ae98-4949-3b0d-a304-a764485e43ea | 0.24016 | -51.48454 | 2025-10-24 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c95325f8-7872-32ad-a1c3-ab596cb357bf | 0.36671 | -50.93377 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa93eb9b-5bb6-34fe-aa90-4e283021e425 | -1.76841 | -54.86168 | 2025-10-24 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd8da849-090e-36ec-8dd1-c742fb477f5b | 1.35318 | -50.92188 | 2025-10-24 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24665940-2efb-300e-bcef-d8e802d1503f | -1.12252 | -48.85893 | 2025-10-24 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9b3939d-bdc1-3548-b605-1b0487e27de4 | 0.3877 | -50.92624 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 595cd937-44d5-3565-93cd-76b2c6174d0b | 1.64524 | -55.76217 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cacde99-ae4f-3d3d-9af0-3f8ca1e00a07 | -2.47329 | -49.23482 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cb2f2c0-40a4-37a3-b165-5892985ca600 | -0.8545 | -48.72803 | 2025-10-24 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 748241cf-da71-3135-83f4-9d9a67a2fb01 | -2.87084 | -45.2567 | 2025-10-24 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cb6ce0c6-fac2-3b5e-82ad-fe9cca353452 | 0.3595 | -50.9349 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01753bc5-f2ab-34e0-be97-71c98ac1edce | -0.85781 | -48.72855 | 2025-10-24 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3fc3fd9-68ad-3c47-ad7e-c4828f91d3af | -2.48086 | -49.01529 | 2025-10-24 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3018eef-359a-354d-ac54-028fda16a2fa | 0.40927 | -51.08566 | 2025-10-24 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e17dccd-8356-3d1a-824f-736f43999d19 | -2.47162 | -49.22386 | 2025-10-24 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e40c0e6c-e641-3e5e-a012-a4115fcfd115 | -3.69934 | -40.42522 | 2025-10-24 04:36:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bc3cfbb2-b3ee-32ea-b841-d0e37773d1f2 | -1.5446 | -55.4138 | 2025-10-24 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23062c4e-ed00-38d6-9501-03f3f991da84 | -1.92721 | -52.14075 | 2025-10-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d64edd25-c95b-3986-b639-2e927ae6cdb7 | -2.41876 | -48.44144 | 2025-10-24 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f71d8a32-13aa-366e-a176-bc8a08a94a22 | -9.9386 | -47.45836 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e270c86-c768-3aba-9de5-9153add3e3a2 | -4.61292 | -50.50433 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e801774e-9dcf-3cd4-934a-ac8cb84e8607 | -9.6085 | -46.90922 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab9329ac-225f-3d7f-930e-e5120d4e804f | -6.51436 | -48.49306 | 2025-10-24 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bc8869f-dc78-3c2c-a7aa-011d7c3ad9e5 | -6.0111 | -45.87667 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37f0df70-b9c7-3f54-a90c-671a76df658c | -8.08672 | -46.91364 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17666fdd-f3d7-32bf-8546-e1177955a8f7 | -7.36534 | -45.02319 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README34.md)
