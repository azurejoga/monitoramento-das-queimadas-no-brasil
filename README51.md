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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b7d30dc-0f39-365e-9eb9-aac29d841374 | -5.41765 | -60.21331 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11bba04c-338b-3af5-aa7b-3c72f188614a | -9.62322 | -43.94037 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6c003cd8-61ae-35c6-8908-998adb6f4049 | -8.91742 | -50.90335 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8b76006-ae2c-3738-8b26-5e7d8055f7cd | -8.6131 | -54.63436 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad692934-68e3-3bff-a738-faae406d98aa | -5.27805 | -49.34019 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2b9e1ce-3f06-37e8-9e5c-e972ff08e01f | -9.68096 | -54.31907 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6df1669-d5e4-3ba2-9f0c-514c869248a7 | -8.5095 | -55.30658 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ee87b751-c5ce-3a67-b637-39eb843b8345 | -7.58348 | -57.67945 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 31d822e1-7bd5-3ffe-98c7-97fc233cd538 | -5.92297 | -51.72091 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0334090b-27f0-397c-9b57-9b43d21b17d4 | -6.5784 | -44.14785 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6fd5e7a3-e557-3bc7-b769-a49a49f78fb9 | -10.55961 | -46.72613 | 2026-09-22 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fd9879e-7a2f-3294-9f4a-2a912da05c77 | -6.7315 | -55.07672 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 792cd077-c293-3561-9f96-69274b290508 | -7.62137 | -57.61316 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b792dc8-cd0a-3464-b329-2801a8abefff | -6.58234 | -44.15331 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5a49e18a-951f-3381-b2a9-108687f75804 | -8.79819 | -44.2746 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e587ee5a-b5e7-3969-bdc5-c70f00358f39 | -6.14309 | -59.94865 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 185c3be6-15a6-34e4-aa85-6f1b6dc96b90 | -7.42718 | -49.84794 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bacd4905-618e-3b36-b631-35a2da522517 | -2.42056 | -58.27708 | 2026-09-22 04:46:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79755b81-809a-3949-98e6-68e9ba3ad5d7 | -8.25146 | -55.27544 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a5d5b9c-cb36-3848-bfe3-1ef6155655f1 | -5.88238 | -52.12967 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b79b58fb-05a9-3e91-be7e-b03f0fe47cdc | -6.42995 | -53.56905 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd7a0737-9d67-3acd-8960-fa3ce12aa121 | -5.91822 | -55.69714 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc778f6d-d759-3d1a-8e5b-cdc4ad6fbfc9 | -8.23177 | -54.68441 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9235046-72cd-3296-8ba0-564a8ef28036 | -6.39576 | -60.02254 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a0a8a63-72b2-3d79-9350-b9d61ab9a6f7 | -3.22954 | -53.9486 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1a919024-9d30-36c2-bae8-319fd823068e | -7.42491 | -49.84008 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0555f8f8-44df-36be-84bb-7345c73968bb | -11.09385 | -48.27679 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28761894-ef57-3a48-b122-3c6af28b8a28 | -3.72099 | -60.58379 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a694b9f5-aa03-3d4a-9123-de85efdfe372 | -6.84459 | -55.26874 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27bd4d86-1c7f-3269-83b8-87de71cc38e4 | -5.8796 | -52.12564 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74dbeede-084a-3b2c-ac8b-9137d57df379 | -10.13031 | -45.54842 | 2026-09-22 04:46:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aea2ad45-d016-3c64-a936-889cf9bd00b3 | -6.12997 | -59.96296 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05d5f317-eb5e-32b1-8f55-b6afe11c4318 | -6.60207 | -39.14433 | 2026-09-22 04:46:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| af3fb6b4-8fa4-3489-bcb5-124c795a6bb1 | -3.24419 | -53.95084 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bfd53015-5014-3f6f-bf97-ed0bc88ba58f | -8.74048 | -52.36681 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cbfcc6f-a633-361d-8c42-2a7120f6b86f | -6.75362 | -59.06947 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbfad6fc-cefe-399d-877e-4fb653b65ac1 | -5.87704 | -51.57877 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b8945e-8135-320a-8ea2-7b255749d5a0 | -6.27943 | -57.74328 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90238e27-612e-36a3-a7fc-044a7774ba5d | -9.68942 | -50.85616 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d80fdcb-09c7-3883-95e7-ae375e4318e6 | -2.54863 | -58.01501 | 2026-09-22 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55770093-c4ae-390a-8c03-a67c70541764 | -7.61015 | -55.33978 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff8cb5fb-e316-3a52-92b6-475c662b82a3 | -9.94951 | -53.98353 | 2026-09-22 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bae67a4-2a1d-3767-babd-317ec124ca3b | -6.16018 | -59.94223 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c14501a-75e4-3722-bb86-12535c1df11f | -3.05821 | -54.40124 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df703cb3-68e4-3693-bf4a-db519f251158 | -8.25302 | -55.27285 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d83f5af9-d604-3f91-9428-e0dda9498ae3 | -6.45917 | -60.03416 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f8aa451-1eaa-32e9-a3fa-fe8b9ecf5305 | -6.19468 | -57.78325 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cb92b375-d7f0-326b-a647-ce242b56faf1 | -10.55041 | -51.29222 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ab0555d-2d6c-33bd-8c82-5812689fec12 | -7.42608 | -49.85511 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c3b4ac1-0292-3a55-8c10-ff9efbf76062 | -5.85643 | -49.7815 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10beb0aa-19c6-3211-be16-2217615f1b57 | -5.41707 | -60.21668 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee9a6671-d5a7-35fd-85c7-c7847c56438b | -3.04539 | -61.25835 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 280bacbc-5ba5-346c-9917-ccda93130d8b | -8.62155 | -54.62738 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1597f21e-ff5f-3c15-8826-418524e29fbc | -6.64014 | -59.92174 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2bfdfa73-e39f-3d8b-b448-dbcf9c514a39 | -5.8991 | -52.28426 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c98e7ceb-30c1-3ca0-983f-de121232271a | -3.90515 | -60.59703 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52baf4d8-7ee5-3888-bdfb-a67adb6d96c6 | -7.8836 | -54.72787 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bf1a776-4615-3dcb-9dc9-c216b3659e22 | -8.79133 | -44.28934 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cc7aab64-2e34-3434-ba1a-5e7ca220a44c | -3.77262 | -51.35265 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2508eedc-fc22-3d5f-908c-6758b62bb6c8 | -8.00424 | -44.80548 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d53cf69d-44d6-3f84-8de1-9098e75cb8c8 | -5.24498 | -49.2311 | 2026-09-22 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87551153-a8fc-337a-ad26-57ab9e5cedfa | -3.05715 | -54.40298 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58944289-9bda-3f26-854c-c3884c1ab996 | -6.66069 | -50.94238 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e55677cb-a679-3132-a9f9-6977082c661c | -9.72384 | -47.77056 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5c29c588-6379-32bc-bf4f-56a3dbcf0c50 | -9.73825 | -48.15311 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c94f13bb-2114-370a-84b8-d2d874c4a716 | -9.68003 | -54.34677 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e345ecb-e31f-3185-bc4a-0001a7833580 | -8.61666 | -54.63495 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 601e9f1d-501e-3f92-9107-2d8ca30a9cb1 | -9.67784 | -54.33831 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa7324f-a0d4-39dd-a7dd-f8ac27875104 | -6.97728 | -42.13315 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d1029b4f-a90d-33c9-83d7-0a6beca6bd54 | -9.38335 | -47.77084 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a238ef4-0efa-3f54-a37c-a8924f5c4043 | -3.4856 | -59.58154 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0770b04-f840-31d7-97fe-766188acc8f1 | -5.73314 | -52.23309 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7fc4e3a-f093-3394-9cf0-6b4be01c762d | -6.64934 | -59.92962 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| b4c91cdf-3a50-3751-9f15-155f64ccd061 | -7.57048 | -57.67726 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 950769e4-8b9c-38c9-a213-19003792d0f7 | -3.80984 | -52.15398 | 2026-09-22 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53c288de-fedd-3e06-b909-f99d719b5e1f | -3.31142 | -57.85907 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63aa85a1-414b-3015-ba83-a6e8944f53b1 | -10.02228 | -45.21318 | 2026-09-22 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 414a1418-02a6-3a19-bec5-3fd369dc7d4b | -3.23621 | -53.95391 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f92b772f-e3ef-324b-a436-b64ff3296a78 | -3.51215 | -59.58154 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 98f4ace6-cf32-3bd8-aaa4-06bbd0723184 | -5.7294 | -53.46416 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bdb458b-987d-32eb-b5de-ef0eec6cb539 | -4.83013 | -45.99004 | 2026-09-22 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee428aba-d53b-3012-a520-8d8cf1dd944b | -6.10445 | -57.68386 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6fcb3463-08dc-3b3a-b215-7a1dd3816149 | -6.00848 | -47.90451 | 2026-09-22 04:46:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1472dd9-4593-3e62-8765-fa518c58b0af | -9.23748 | -46.16544 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d92590e-80dd-36ee-b3c7-70a6f293f2ef | -6.25454 | -55.48113 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cca170a-b831-3128-bb07-3696de3ab081 | -5.65097 | -43.41857 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67bbaaa0-dd85-3904-b521-bbb38ba2cc25 | -3.37931 | -50.40945 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0de6cfd0-bb01-33b6-a596-5b45806f3f0d | -3.26107 | -54.26925 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03483aea-550f-334c-b14e-8dcbde373523 | -7.23694 | -45.83062 | 2026-09-22 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b66a2825-2777-3fdd-a11c-35f41c140851 | -6.84383 | -55.2733 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44f04d85-c6b8-3432-ad69-27267722e011 | -11.10734 | -48.31746 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17927065-bd26-3391-a5a2-14bdb185ed27 | -9.68034 | -54.32289 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5734af1-2b3e-37d3-8aff-df0e09ee05ac | -6.19022 | -45.32273 | 2026-09-22 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc70b5a7-b08e-30a8-a2f4-929d3db9aa1a | -2.93732 | -57.80685 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 91d2d9f5-2808-32fa-9ff2-7bd96a9baab7 | -6.94045 | -42.90944 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1fe9d22-6dbe-33f5-80dd-482bef079708 | -5.86033 | -49.77844 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1bbfaf9f-f3a4-34f1-978d-8f3bbb9f885b | -10.45776 | -45.10337 | 2026-09-22 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f93b74a-d156-3b28-8acf-a4f7c619bfd3 | -8.31569 | -44.74844 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6d792d8-8620-36b3-aa70-410266f929c4 | -8.53916 | -54.6896 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 439b5aea-ea4c-3f9d-b78b-57ce1ed1a8f2 | -10.872 | -50.15752 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README52.md)
