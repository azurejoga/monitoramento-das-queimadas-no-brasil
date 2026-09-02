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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd452fb8-1aa5-3dc3-a32f-9a9008758b92 | -6.12514 | -57.74267 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adb2e9fa-22bf-3576-8881-ff6b2bef54fd | -4.95851 | -55.85517 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60b30e86-a3ba-35dc-9170-952f71851976 | -6.93415 | -59.64077 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e24ab8c2-69e1-3492-89d5-c5a10e23bc05 | -7.1926 | -60.6893 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02c159c0-4f8b-36cd-9520-c0ab0d773bfa | -1.4708 | -54.82709 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f6f9663-1e58-31d0-95e5-1385d9459d13 | -6.24764 | -55.42634 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 879cfab9-08ef-3d5e-932d-78513b172de6 | -6.78109 | -56.29594 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b217cb83-5a06-3e9d-a0b1-86bc98ea5724 | -6.69195 | -59.94338 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb094ad4-4d99-3a97-8693-a699010cfcac | -5.88943 | -57.75093 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b4928ca-df10-3e29-a06e-dd9f429c655c | -3.61822 | -60.56335 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ba1a1ce-f275-371e-b508-dc5c0fb4d7cd | -6.7624 | -59.44597 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad7c2588-8b4a-3913-bfc5-f4f327ee8a2e | -6.08827 | -53.80577 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e69ebfc3-b972-31f7-abcf-c5e1cb6adc7a | -9.66112 | -46.5308 | 2026-09-02 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c6d68af-7255-38f2-b170-5107a257dc4b | -8.11299 | -54.95666 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbcbbf79-ca88-340b-b19d-0fda8ecf7524 | -6.81116 | -59.10261 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b4f798a-d874-3080-bff0-d6eedfbb4e78 | -6.62911 | -55.30738 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1c34108-3345-3ab1-b6a3-274d6a22873c | -6.14565 | -55.67778 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3f05bf3-fa2b-386a-a904-a123b42e7b6b | -5.8523 | -57.5574 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8e34738-3305-303f-9dc8-1b0e51a68b96 | -6.94954 | -56.45407 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38036e06-7efe-30e1-9c0b-73adc972c974 | -2.32852 | -60.06665 | 2026-09-02 05:16:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 939399d0-25ae-3fa2-a040-e5821b7af682 | -3.06747 | -61.21916 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9358a25-4580-317e-bd5e-7e32d28dd20b | -7.57773 | -60.46531 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71a90240-9440-3ff1-aff6-74b12bf39dda | -6.15021 | -55.67087 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9052d09-f25f-3901-8684-047af524d344 | -6.12231 | -57.67489 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cab7837-233f-3440-8090-8a6fa9c0818a | -10.32189 | -49.94326 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62ed2493-452c-394c-941f-50b9d128a95c | -8.69266 | -62.9315 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44ffd215-050b-3491-954f-5540f77afe54 | -11.30954 | -45.15017 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00b2a2f7-3495-3fea-97e8-6d741849d3e3 | -10.44309 | -46.7141 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b9535a31-42e9-3fc5-b03c-6c40ae3b7701 | -11.48314 | -45.09469 | 2026-09-02 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 969d78e2-8f84-3eed-b752-f2b1e767764a | -9.92878 | -60.48351 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb57f006-ab1b-35e1-8e07-ec513e4a165e | -12.14264 | -47.0743 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d1c7bff-3b95-3b34-a896-bb2884a6b978 | -11.29772 | -45.19074 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb2be98e-7525-327d-9c3f-32cd4e4084e3 | -12.14731 | -47.06474 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8a1bfc8-913a-32ee-b426-b06814a46db3 | -11.67323 | -50.19976 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ddac220-e1c2-33f9-a7e1-1126cc4ef310 | -8.78097 | -62.48454 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfae499b-e01b-3844-95bd-98841f04498b | -10.9649 | -50.48698 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9c962d3-575b-3118-825a-cf4c986d1778 | -11.4839 | -45.08803 | 2026-09-02 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9925acae-933f-3fe1-b67b-1bdd1a0cd46b | -7.69329 | -67.12386 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e5a6c7c-1f60-3f79-b076-46aebb31057f | -7.9436 | -63.44823 | 2026-09-02 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32f7b9ed-33c0-39cf-ac82-2bc662bcc3c7 | -9.08413 | -65.37998 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac4c048a-e5fc-3bdf-a704-91be2b391a5b | -10.27831 | -60.53664 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fc587e9-acd2-34ec-a6ba-b0d724c10e07 | -10.5043 | -59.61897 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba5c45cb-88f7-3aaa-a3bf-e6a2bd9df5d4 | -9.92959 | -60.48434 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c186dfb-d082-3130-8b44-e9b7687f9cf3 | -12.13123 | -47.06273 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67db6468-d381-3fc7-8855-9d1720317d7f | -9.39662 | -51.69232 | 2026-09-02 05:18:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fde31780-16c9-3ee8-aa0b-5d662ef805ff | -9.86435 | -64.97617 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 794001fb-8699-3db7-a66b-19ddf29e22e5 | -11.29937 | -45.17659 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e296c151-1c55-3eef-92e6-80d7aefc0ffb | -11.3019 | -45.15483 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2992e3c6-a4e1-3cfe-a2f1-7e5ff8f45f4d | -9.09072 | -65.37924 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| da4776a9-2f86-3ab9-8b2a-971890e7b69d | -7.84434 | -61.13937 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9618af68-24e5-31fa-a749-3b6c810359be | -11.29698 | -45.18872 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c628896-8cba-34c7-8fe9-755f1bf0074a | -12.14204 | -47.07933 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e6c9a5c-9915-3e92-9b99-a6e5d1f2f9d0 | -8.74675 | -62.56866 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b9c0ecf6-054b-351a-9597-ed20895cf49e | -9.86958 | -64.97254 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3205ea21-430a-3ea9-82c8-77f367e8fe10 | -8.1027 | -58.27585 | 2026-09-02 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa194f83-fb24-3cd9-bfbf-14fcebff0ef6 | -9.46623 | -56.74079 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b344937f-5828-36f0-99fa-05ddc4edc2a6 | -10.40763 | -50.00089 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f04accc6-3f12-31ed-b4e1-853ecd24020e | -11.31483 | -45.15532 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbcaf70c-b8a1-3a22-8815-d992ec02d4a7 | -9.8688 | -64.97697 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd68ecc9-6237-3407-b9a7-09b9cd481f18 | -12.14323 | -47.0693 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27849832-be97-33e5-8291-6ec709156cfd | -10.31411 | -50.04313 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f48b7c78-7730-3def-82a4-55b5614d9e20 | -12.15135 | -47.14174 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6021430-59b8-3ba6-afd3-27a41fe20352 | -9.69558 | -47.20917 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46fb51de-f2f2-3f16-9b9d-3552cb9c2b81 | -7.6904 | -67.12663 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39bfaf2b-70d6-394f-a765-6e0e5262c395 | -11.30265 | -45.14844 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ecbdea1-08a7-392e-a474-2448944ca596 | -9.0134 | -65.41029 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 738a98b9-a3ac-3f93-b829-e39f6185b3a7 | -12.14618 | -47.07476 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cfed0dc-2392-34dd-8b83-91c40d026f3d | -9.08876 | -65.38083 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 973cccde-7caa-3674-8c73-1cbd371737f9 | -9.83019 | -59.47631 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d71751b3-2786-3736-9b67-6b6e5029c744 | -9.39571 | -51.60161 | 2026-09-02 05:18:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7125ea57-6450-331a-96b6-36d04410bf5f | -12.13995 | -47.12999 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d0a6f99c-9b22-3b80-b55c-fffd1e705349 | -12.37703 | -48.14631 | 2026-09-02 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe50ae3a-7f1d-3814-b34a-260cd9615175 | -7.77078 | -61.2009 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52c3a715-9ebe-3f10-abe7-dc8f6edcd455 | -9.4417 | -67.42162 | 2026-09-02 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5979ca03-d783-31af-9642-b34eeda26f1e | -12.13142 | -47.14922 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| fa1cf5e8-c014-3720-95b5-1cbfcf8d52d2 | -9.21931 | -59.76194 | 2026-09-02 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54e58dc8-6fb7-3ccb-9dc8-bd8e3acd2a2f | -9.22808 | -59.7934 | 2026-09-02 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cb43c38-02e6-30ba-8475-97685fe20656 | -9.8769 | -64.98306 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16aba021-a85b-3a66-8ba7-783aa8ca667d | -10.39277 | -49.99583 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bc3f341-f673-3da5-939b-ec76a0c5af43 | -10.04388 | -48.69268 | 2026-09-02 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3926480d-40e7-3142-936a-1bef1743471a | -12.14383 | -47.06432 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14bd14eb-9009-370e-8109-7e6fdfa1c26e | -9.47661 | -57.0314 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa75695e-5c70-3f9a-abbf-1df0b9f01633 | -10.49542 | -59.61013 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7171660b-55b4-3119-8420-347e030b7652 | -11.34771 | -50.63436 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34ff8904-a2b4-3285-a536-dd5f49cda714 | -11.66888 | -50.19296 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92506172-b60f-34db-8eca-7836610768e4 | -9.712 | -54.33622 | 2026-09-02 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00092c57-9765-349d-a323-b50809978bd1 | -12.13591 | -47.10929 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c5ba3cb-348c-36b4-8d57-b6d1d1c8cd70 | -15.59857 | -46.57904 | 2026-09-02 05:18:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e2165930-5d98-3b75-a162-b1f6f64c243d | -10.87965 | -45.34914 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57428dce-a508-3239-a2b8-25382bff9bb9 | -12.13882 | -47.14001 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8699a85f-268b-3639-9ab4-dd1db8b42067 | -10.30943 | -50.03945 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccac6ac7-5724-3623-8fba-04b7414027ee | -8.69717 | -54.69408 | 2026-09-02 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d4eaf5e-0cd6-3c09-8a81-6e9616c1a0c0 | -10.41033 | -50.00502 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ccbcbb54-f55c-3d24-98ca-bed65574bb1c | -11.67646 | -58.61628 | 2026-09-02 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 961db66f-b71c-368c-908b-8ba890430e2c | -12.13938 | -47.13499 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d5519271-7f0f-3abd-9dd1-1c6e2879ef06 | -11.3064 | -45.17704 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e7c0030-0b25-330f-bf58-293761a42aee | -11.34845 | -50.62872 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66666587-07a0-336a-9eaa-20e1db2f99c2 | -15.36231 | -47.04313 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20401c62-6e0c-3d26-9656-0c1fea801273 | -15.34869 | -47.04667 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76bc0e53-ae95-3da9-8e57-6f72b70d8e0f | -7.69388 | -67.12051 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README55.md)
