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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35013a23-8ad9-3c41-976c-3c8846492896 | -16.32402 | -40.26382 | 2026-10-05 17:11:00 | NPP-375 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 89fbb0eb-f5b2-3043-8826-48cf77105738 | -17.89095 | -39.42656 | 2026-10-05 17:11:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 95c363cf-7ec6-3ce0-a0b6-acbe5826c511 | -18.02241 | -41.66847 | 2026-10-05 17:11:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| bebacb75-4ad6-38e9-b128-a266816b6777 | -16.53741 | -41.4967 | 2026-10-05 17:11:00 | NPP-375 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bcdafa9b-6ebc-3a77-bd3f-a1b81ed66034 | -17.92765 | -39.42286 | 2026-10-05 17:11:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 812be3be-a316-3426-9be6-4bf5755b6c13 | -17.68499 | -44.75685 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5643b7d3-8f97-3715-90fc-95119abce73a | -17.42621 | -44.97111 | 2026-10-05 17:11:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ae8f06b-0a58-3091-bcf3-a2172d8327b8 | -18.12411 | -42.93761 | 2026-10-05 17:11:00 | NPP-375 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a3e11c3c-a2fe-38a6-802a-59b822d5afab | -19.12273 | -41.06833 | 2026-10-05 17:11:00 | NPP-375 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| d2ce5c72-bdc0-3caf-92f9-8c4fb1ad2c3d | -18.02688 | -41.66394 | 2026-10-05 17:11:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e3119c0b-294d-3dc9-ac63-7622c9abf38b | -17.68928 | -44.75601 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4875f8f2-1c6b-3f2f-bbdb-890ec748bfc9 | -16.57511 | -41.59199 | 2026-10-05 17:11:00 | NPP-375 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7da74388-df7b-3521-b959-e576d26233e6 | -17.8969 | -39.42518 | 2026-10-05 17:11:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 95697252-425a-338e-a18e-d015a0e6e141 | -16.83038 | -42.22401 | 2026-10-05 17:11:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 31bcb53b-69a8-33e0-9afc-8d0bf0d08fa6 | -16.56903 | -40.51155 | 2026-10-05 17:11:00 | NPP-375 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9a53f186-1233-3c2b-840d-c4a85898d201 | -17.40115 | -44.95462 | 2026-10-05 17:11:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ace68bb9-67c0-309a-b96e-e8dddd750ab3 | -16.69357 | -42.5139 | 2026-10-05 17:11:00 | NPP-375 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b37bede1-d445-3b8a-8b59-1281a51dd853 | -16.86295 | -41.03031 | 2026-10-05 17:11:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 77ff709f-b0ba-3465-939f-95ef5145f9ef | -17.68365 | -42.18019 | 2026-10-05 17:11:00 | NPP-375 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 0e56b9a5-85e4-37ea-9c38-2400238746ea | -17.67912 | -44.74921 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 31bb1ca9-c4b8-341f-86f2-2ee2253b0459 | -18.36536 | -41.77984 | 2026-10-05 17:11:00 | NPP-375 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b2d56fff-c83d-3809-aae6-262ecb72fc40 | -17.54997 | -42.12056 | 2026-10-05 17:11:00 | NPP-375 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c46bab92-d1fc-3813-896e-742cfa0d55f0 | -17.67403 | -44.74577 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a0d65e20-f171-374a-a3c0-ff83a3ceadd5 | -17.89195 | -39.43113 | 2026-10-05 17:11:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 7a8b371e-535a-31de-864f-dc0e7956abd2 | -17.42197 | -44.97197 | 2026-10-05 17:11:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5cced2c9-a8ad-3277-8e7e-1a95fd48d2a2 | -18.0218 | -41.66556 | 2026-10-05 17:11:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f38e569f-42d6-331f-951a-b3902f8029ae | -16.82974 | -42.22092 | 2026-10-05 17:11:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 564cf221-9e89-3478-aa1d-174287187d4c | -18.99918 | -41.048 | 2026-10-05 17:11:00 | NPP-375 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6a22e30d-7780-360f-b0af-01f3559d816c | -17.68848 | -44.75176 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fc5a2f8-d042-388c-a099-e78894943fd4 | -16.57328 | -41.59117 | 2026-10-05 17:11:00 | NPP-375 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3f23728f-2400-39de-8320-de1db91d4959 | -17.67482 | -44.74999 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6825941a-569e-3e7c-b089-1103b2e08434 | -12.16457 | -60.74968 | 2026-10-05 17:13:00 | NPP-375 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1055b67-5758-3742-a7f9-d2e307f16864 | -10.24722 | -49.65213 | 2026-10-05 17:13:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1866484-b204-36e3-a9ec-ebf181d4fd5d | -12.81068 | -43.31858 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0d243ff1-aa19-3e76-896a-d26101148514 | -14.6146 | -41.38672 | 2026-10-05 17:13:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a16b466c-6573-3240-9296-8f6c3e808922 | -11.27844 | -44.28922 | 2026-10-05 17:13:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| d803a6b7-6ebf-38ca-b730-2ac9e18df60a | -10.49098 | -47.24026 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 394c10b2-61c0-3ab9-b2a0-e814b0e52e71 | -11.34229 | -46.67826 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 529874d6-0df2-3653-8b19-f3fbd3ef4087 | -10.4038 | -47.53991 | 2026-10-05 17:13:00 | NPP-375 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 4a7af210-cc9d-3931-b31b-393daa1245e5 | -14.99178 | -41.72915 | 2026-10-05 17:13:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b19e017f-7709-3381-bb5a-7dd8ccc66217 | -10.02573 | -45.41014 | 2026-10-05 17:13:00 | NPP-375 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ebfbc0fb-e04a-39d1-a433-e32940057a12 | -13.75103 | -43.62134 | 2026-10-05 17:13:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a35f9edf-3a8f-3baf-b4ee-9c960e860e66 | -14.63438 | -40.57133 | 2026-10-05 17:13:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f3496422-9cd8-39b4-af9d-429b401bc3ae | -16.55498 | -56.24086 | 2026-10-05 17:13:00 | NPP-375 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 13e9ce46-926c-3201-a86d-6441535b9b8e | -14.92118 | -41.41369 | 2026-10-05 17:13:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e735ae87-fb89-3a0d-82c9-86a0f52a7704 | -15.69013 | -39.7947 | 2026-10-05 17:13:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 21e32395-0d2f-35b5-8d22-d3ef77521bd5 | -15.69618 | -39.79326 | 2026-10-05 17:13:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4c557a13-3ab4-3567-82dd-9b269cd6f5e2 | -14.28107 | -43.75906 | 2026-10-05 17:13:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bb03df74-3e4a-3d7a-8041-64e1a6e86a3f | -14.52671 | -41.56855 | 2026-10-05 17:13:00 | NPP-375 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3006e9b0-a8ac-3e7e-9e34-2e6eaa093a52 | -12.02653 | -62.53877 | 2026-10-05 17:13:00 | NPP-375 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aec32ab7-2d2f-37ce-a738-f3431fab4edc | -12.24738 | -42.11259 | 2026-10-05 17:13:00 | NPP-375 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6b2f9da9-4015-38a1-bf13-f32d9777a692 | -12.13211 | -61.14719 | 2026-10-05 17:13:00 | NPP-375 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 636c9870-f9fe-3970-94c8-19334545f697 | -11.07482 | -47.49321 | 2026-10-05 17:13:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 997086e3-a788-3aff-a21f-c3491f9d1401 | -11.4394 | -47.68661 | 2026-10-05 17:13:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d35d8d81-ecf9-3527-9fe3-0b8952b35515 | -11.71495 | -43.42921 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fa13d59f-c72b-3836-b730-8a1551006efe | -13.16324 | -43.09912 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 155f45f6-3958-3137-bea1-12023b43c68a | -14.37148 | -41.89548 | 2026-10-05 17:13:00 | NPP-375 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 46e4f0c4-668f-3af9-8222-b1279cbc915b | -11.33932 | -51.30361 | 2026-10-05 17:13:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ef0c29ff-893d-3a1e-b6fd-2b97ea9ac306 | -13.50462 | -40.8406 | 2026-10-05 17:13:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 135.9 |
| 8094fcaf-f329-3ac4-858f-cf14b298f56a | -14.08108 | -43.76418 | 2026-10-05 17:13:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| db56652a-b960-3e21-9118-eaa4c40ae386 | -13.32731 | -39.07027 | 2026-10-05 17:13:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a2b20e8f-0b0c-34f3-bfa8-6567b37a8d96 | -9.79762 | -44.79082 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 73240f70-839b-3737-a0ac-fb6ba7caf565 | -16.54697 | -56.24199 | 2026-10-05 17:13:00 | NPP-375 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| c37f738a-ba97-3b03-a0da-a9421b764e52 | -10.95771 | -45.42528 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 78a6e451-47dd-3b87-ba0b-e9e322d735c0 | -11.34511 | -46.6694 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c373fcaa-f5a6-3652-b3ca-08c36b38ff8e | -13.14095 | -47.72255 | 2026-10-05 17:13:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edbc57ed-b336-3fbc-b189-f79d9e7535c9 | -11.6348 | -43.60731 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0a0b1b6f-5623-3e51-bc4f-4c62d8a018d3 | -11.68079 | -43.65429 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7d3ee00b-3d2a-3c50-a12a-34cbbe35b507 | -11.72292 | -43.50045 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| bdcb4bdf-3c7d-3d0f-bd1f-83651ad00822 | -10.97312 | -45.43136 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ac0fcdd8-0a80-32b2-b0cc-72f58ed97597 | -15.6903 | -41.41893 | 2026-10-05 17:13:00 | NPP-375 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 94f6b5ff-cd1a-30fa-85b0-58eecedafa8b | -15.91242 | -40.98339 | 2026-10-05 17:13:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 85ea3cae-9105-39b6-bebb-55be322c83fb | -16.03806 | -45.08609 | 2026-10-05 17:13:00 | NPP-375 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5722319e-426d-3b81-ae13-94c7c97e0ccf | -11.20124 | -47.14052 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d02f67b1-e288-3ed5-b059-8f80716173e3 | -8.52809 | -39.54829 | 2026-10-05 17:13:00 | NPP-375 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 4db167ee-12b5-3e87-95af-d3eaeeb64037 | -15.57754 | -41.50388 | 2026-10-05 17:13:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5f884cba-9912-3727-8197-b95905979023 | -11.22184 | -47.13727 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d09e3691-ed66-3425-a6ae-1d447a8986ce | -13.15277 | -47.74554 | 2026-10-05 17:13:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 68febc8e-a133-3e75-81a6-edc843b21ddf | -11.73625 | -43.51435 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f003121-3494-3825-ac7d-16cdaf1fcc6e | -14.55563 | -41.70535 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f0245c48-4ed5-3414-909d-f1fd1ad4c696 | -11.65151 | -43.6111 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 915fc928-76f8-3429-895d-05c4bed1c65c | -10.2307 | -46.6569 | 2026-10-05 17:13:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 188d612b-7408-3e73-b70d-35b969003e8b | -13.64669 | -40.87544 | 2026-10-05 17:13:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 86eaf415-f4af-382b-8802-81cf8cedde08 | -14.55734 | -41.2863 | 2026-10-05 17:13:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ad54c450-7e02-3a31-96ff-df00c39bc786 | -10.17445 | -45.19846 | 2026-10-05 17:13:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3353959-f79b-34cc-ab3a-d2bb0a5f3dcd | -13.07278 | -48.60515 | 2026-10-05 17:13:00 | NPP-375 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7fe1ca69-ef7b-3226-8345-6bc91bcf32a5 | -10.36966 | -48.09777 | 2026-10-05 17:13:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1555f356-9ef8-3b08-aeee-0cb5d9e7e8fa | -12.0419 | -41.13802 | 2026-10-05 17:13:00 | NPP-375 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2c0323f8-ebb2-3db0-b8ee-dd3039a75a20 | -10.24706 | -49.65614 | 2026-10-05 17:13:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c142d1c6-2bf4-36da-81fe-fcdf174eacb5 | -13.50819 | -40.84468 | 2026-10-05 17:13:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 85a46d9e-5640-3d2c-9188-90b6697d6f8c | -14.92042 | -41.41002 | 2026-10-05 17:13:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 690362a0-4c42-3d0e-9483-1c4795abb517 | -12.81005 | -43.30964 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| b319fcf9-5858-31e1-91d3-0e82e3b76745 | -14.98133 | -41.56554 | 2026-10-05 17:13:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 00f94d8b-8ad3-3265-8c3a-df6c7aef870f | -10.96966 | -45.4122 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e4317fd7-b449-35c8-a854-64917a8217ad | -9.8554 | -44.79586 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4bf5d4f9-00a5-3d7e-821a-40fcaf9e6e4e | -13.64108 | -42.10588 | 2026-10-05 17:13:00 | NPP-375 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5325558e-ca7e-3cfe-86ef-667e9b589ca0 | -11.82492 | -48.21906 | 2026-10-05 17:13:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84c32355-4f67-337d-a8a4-25cdcd8b56c9 | -14.83284 | -41.72945 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 106ef674-919f-364d-bc87-339b0053cca0 | -14.21308 | -41.59298 | 2026-10-05 17:13:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e057886c-e224-35fc-9661-2bb25cedfe18 | -11.82035 | -43.53195 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README103.md)
