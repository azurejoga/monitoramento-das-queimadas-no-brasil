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
| a66cd958-5d6a-3993-bf85-88813288a63f | -14.68747 | -45.18591 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33e68faa-efba-3a9c-ab14-ba0cde29c92d | -19.58699 | -45.8973 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 815d05f2-5ccc-3605-a1c9-c867e1fa9fa6 | -13.76344 | -47.53714 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9002bb8-a969-3722-9202-d1553ed5784d | -13.91734 | -48.07136 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cb09885-f3c5-39d1-9d61-d1d3e37c596a | -14.9334 | -46.89601 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6f86a21f-08ce-3931-9f8e-b915758304c3 | -14.68385 | -48.0922 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 158a9252-9f62-3219-9500-c37139c8f802 | -14.406 | -46.17355 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33e02abb-308b-38f9-958c-dc231d776085 | -14.86835 | -48.3067 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f33a3d95-8c56-311e-be22-9b069d4aa1dd | -12.3749 | -46.52314 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03b91e99-4e4e-3ee1-aebc-bf7d31f29926 | -15.24895 | -47.91721 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6e8dd72-ed51-361a-8885-61b9b6dceecc | -20.13288 | -44.00869 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8354d039-57d7-3168-86ab-85ab2607b52d | -14.18739 | -46.6892 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d000cd73-69da-3028-8acc-1b51696a835d | -14.46076 | -48.40369 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26f659f5-ef68-3924-9ee0-56143e2aa117 | -20.37095 | -42.20609 | 2025-10-03 04:34:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 81d54cde-d48e-363d-aec7-12afeb647c63 | -13.97405 | -48.16238 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7e0c194-6523-3f3b-805e-f922be772725 | -13.74918 | -47.95452 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b9fbd2d-77f1-3075-8355-362332288c4b | -14.43672 | -46.37174 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 233c5a11-e1a6-398d-8dc3-a99b99f19b0c | -14.73761 | -48.1343 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 657e87ec-c294-3ebf-924b-01cd6fd6755f | -13.30906 | -47.25506 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d84203d2-e603-3619-996d-926aa7d9728f | -13.12144 | -47.86922 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 496be0c7-3f34-3370-ac39-1ed64f050359 | -14.43424 | -46.10639 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d701c9-0f1d-3e35-af4f-d87fa577b26b | -13.19247 | -47.81997 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 406eb11b-04d7-3e04-bb0e-6a97e842c387 | -13.76923 | -48.05908 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 379e9352-9e8d-321f-bf0c-a9b87ae1a3c6 | -12.59142 | -49.88865 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10e676e9-b892-32ab-a4e1-46da5698670e | -14.42142 | -46.09137 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e49ffb5-0132-30fe-854c-893f8bae464e | -13.76138 | -48.06543 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3594345d-823c-3bed-8cba-893b72b2651c | -13.12535 | -47.88869 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8e82904-6681-3414-885d-222178a840be | -16.04353 | -51.02711 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32689e3a-d2b5-355e-81b1-473e57a3057f | -12.86951 | -47.03535 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9002ca2d-096e-383d-b072-222ba5c09efa | -16.27117 | -47.10304 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ba047f9-db2a-34a5-856e-1fa82e6d7be8 | -14.20228 | -46.11158 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 78acae55-4c4b-3873-9a1d-69e8702d68d7 | -13.64478 | -47.18577 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96d0a36e-261b-3e08-befb-3ae946b7461e | -13.76926 | -47.56835 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1cd8509f-2f04-3d80-ae8a-662110499040 | -14.11559 | -44.31234 | 2025-10-03 04:34:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03ed375d-b27a-3142-a4eb-15335b055db9 | -13.48385 | -47.2535 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8c49c6e-5e9b-314c-9da9-60b9a504ae83 | -13.23828 | -47.30549 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 906be0fe-ec9a-34d4-a45b-ec0ff6c4acf5 | -14.21661 | -44.94976 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e21a6a18-7047-3cdc-bc56-373f86ebc7f5 | -13.12479 | -47.89234 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a041acb-ecc2-3395-8702-2e6f3b1ebf1c | -13.97566 | -48.12897 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e898d55-ac7f-341f-9345-f98e98e00ff7 | -13.76686 | -47.53764 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3955bf38-18c9-3e4c-9bf6-c27a0803cf3f | -14.7437 | -48.11684 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74cd8a71-449b-3077-9601-22ad770e7cfa | -16.26765 | -47.86268 | 2025-10-03 04:34:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a7e60af-ca50-3c49-b808-6705cd13c3f1 | -14.79342 | -42.83068 | 2025-10-03 04:34:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2e633dc-a2ae-3690-ba07-c8842940033d | -14.3553 | -46.13603 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05976455-0b74-3bd1-953b-af31a4de5663 | -13.35606 | -48.0808 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3f3bc7d-aa8d-3104-b9c3-cc37236640e0 | -14.87486 | -49.71212 | 2025-10-03 04:34:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5528f4d1-6328-325b-ae16-6788d4542990 | -14.58077 | -52.46198 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b37f043-d57c-3a1e-99ba-a4a0ddc1e648 | -15.33536 | -46.29592 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36df5c3d-a52a-33b1-81da-ac7c23777b2c | -14.90198 | -48.28957 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ca44e3e-b113-3fb6-806c-ca9546676607 | -18.19967 | -53.35466 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9cd8af9-5642-3db8-bc91-fd6f7aeabcfa | -13.32878 | -47.79673 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db096b17-86b4-3b8f-a0c3-054eb0722738 | -14.73023 | -48.11427 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88fd84f9-28b0-38c5-a8e3-57def5127006 | -11.20775 | -54.09063 | 2025-10-03 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cef5f2e1-72a1-351c-892b-45fb84e8be91 | -13.9724 | -48.17327 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34bbec97-0f40-3dd3-9e2c-7defceea0736 | -12.16766 | -51.41221 | 2025-10-03 04:34:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9bd08c9-3fe1-3075-a863-929e728e2906 | -12.85126 | -46.8597 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 247247b7-68a8-3521-8d18-cd586a549dfa | -14.93456 | -46.88798 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5d1b7af9-8bee-3540-b3b4-ee749f21a411 | -13.30963 | -47.25125 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d864d3ba-95ff-3ae8-b3aa-d2b05ace8b1c | -19.86877 | -43.64909 | 2025-10-03 04:34:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fb73ed40-a7b5-3661-9f35-487991251174 | -18.40116 | -50.77859 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| deec3e7d-6387-3222-94d9-85aa69cb76d5 | -17.99172 | -45.02882 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f51ca411-6c39-31fa-889e-729e1f247232 | -15.59221 | -46.90491 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90232663-d7f3-306c-9fe2-290fe03baebc | -14.73468 | -48.1077 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5c3c085-02cf-30e5-9e41-65950fa4902f | -12.60715 | -46.97012 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 566a1364-0b28-36cc-976f-39c1e2eb1cff | -12.75506 | -50.55499 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 936cf784-4f6f-33ac-a8ca-3709f1846594 | -13.30054 | -47.26497 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeefc448-2445-3302-a716-82361f328f9b | -15.23319 | -48.71605 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5249edd-6069-342a-8d32-9cddac7137a0 | -18.21099 | -53.35246 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6bb9d00-af19-3caa-9f04-6b4fb9f0cd5b | -15.71203 | -46.27008 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f11a6d1-c0bb-31fa-9c90-ce1dea62b133 | -14.19852 | -47.00911 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 549bbe45-5c60-34cd-93ef-29d4aed024dd | -12.63028 | -46.97254 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d29326e2-485a-3c48-aa7e-828c06fb279a | -13.47305 | -47.23122 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68410547-31bb-3ce4-bcd5-4bfb84925d9e | -12.62494 | -46.9693 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ba319e-2317-3252-ba56-930595fce893 | -12.92412 | -47.80822 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1d14ba3-1e26-3536-a090-2d7843bcc95b | -13.12928 | -47.88557 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0d3a99e-1756-3fa7-b2fe-79bd414fe587 | -14.74765 | -48.11357 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| de91be9e-bda2-3ae7-8cb3-4742b99cc0ed | -14.85999 | -48.36174 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52fae09f-b243-31d2-8172-5275076ccb7c | -13.7514 | -47.98525 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc89c971-8720-32cc-a198-f8c0fd8a7d88 | -18.1926 | -53.3533 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e601e58-dd71-3caa-8fd9-564e87f873b1 | -14.22733 | -46.09288 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dc44ce6-9df9-34f2-a0d0-84efb810d823 | -13.77383 | -47.58453 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7579f989-1bdd-36c0-a654-3d0bd118704a | -14.11498 | -45.65942 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0de92e7e-f7ba-39ec-8289-b2f93782600b | -13.32297 | -47.5825 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3218fdb5-e844-3994-955d-4f4065c7e74e | -18.19221 | -53.2921 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccbee465-79b7-3930-a410-e23516ee8b2f | -18.22014 | -53.36293 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7681dce2-d3de-30df-bf76-d4e4532b0160 | -14.85375 | -48.28925 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e01e5f14-a0f1-3074-9a6b-e5e930b1a490 | -14.43973 | -46.37643 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 266b1d32-4082-3692-9909-c550014c1f94 | -14.90362 | -48.34657 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f52a066-5460-36eb-8ed1-108c75afb277 | -19.45485 | -43.65108 | 2025-10-03 04:34:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d282798-4089-39f0-8bfd-87b415d39a43 | -12.80789 | -46.86453 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2081a9b3-bf64-3901-a9c7-8393ef539b1b | -14.91882 | -48.30318 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fd0a0f6-0d98-38d4-9220-c31a87b7631b | -14.45309 | -46.34181 | 2025-10-03 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24309932-a0e5-36fa-96af-fa02447bb3d0 | -14.87675 | -48.34207 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8dda18c-a3ee-392f-a675-f85b1b7d0ac7 | -14.74598 | -48.12466 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ac8c219-1c77-3f2f-8e72-a23aaf22c5cb | -13.33987 | -48.09685 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55ef37cc-5b9c-33ec-a47d-8dcb0cd634a9 | -19.97114 | -41.65711 | 2025-10-03 04:34:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fe0851ae-b080-3883-b926-98863a574409 | -15.32878 | -47.32918 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c958c3c9-223d-3876-a900-05fc9be7fc1b | -12.37433 | -46.52708 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64941a13-90b3-3242-b559-52c8cc77758e | -13.18297 | -47.88259 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca0dd373-cb18-309b-81b1-29b4e5e32eaa | -13.77154 | -47.57651 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README130.md)
