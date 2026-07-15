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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfed6345-d5bc-3606-bbb8-a78e96f3ca0a | -0.08978 | -51.28098 | 2026-07-15 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3648b944-9c43-3921-b1c9-782570e7269a | -5.83298 | -43.58911 | 2026-07-15 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd4b9669-d41a-3751-a0ee-8b0236a47d73 | -1.66784 | -54.46035 | 2026-07-15 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46036d10-83a4-362c-9a14-76b762fb4824 | -5.01928 | -37.5441 | 2026-07-15 04:38:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0433b21f-6c03-3c25-bacf-0463c17ca70e | -1.66414 | -54.45564 | 2026-07-15 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5c9196-9bb8-3ed0-a24b-0ba12fa7aee1 | -3.94631 | -47.26609 | 2026-07-15 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40bbb71c-dbed-39ca-bae3-626c98295195 | -3.22135 | -49.47997 | 2026-07-15 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b97310c2-8e29-36c8-a0b3-67c2ccb231d1 | -5.83243 | -43.59289 | 2026-07-15 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c08078d9-12fa-370d-9a45-3b58f92510f3 | -3.09449 | -49.35667 | 2026-07-15 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 263e467e-c364-35d3-9f9f-d1ecffbce3c8 | -1.59017 | -50.43508 | 2026-07-15 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db4dc9d2-f51a-3039-af17-65b33bde309d | -3.94293 | -47.26559 | 2026-07-15 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26181280-fea7-3176-80b9-ee6902e0f426 | -4.6573 | -43.22922 | 2026-07-15 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41f8f30b-1e50-34dc-b2f0-19391366a644 | -13.4368 | -43.84666 | 2026-07-15 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d96ff3dc-2328-3231-911a-6f239d5d0afb | -8.21397 | -49.47205 | 2026-07-15 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2a3f3f8-18ca-3db9-bb1c-258dcb955062 | -12.44541 | -49.58986 | 2026-07-15 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fc6e2fb-a60b-3d82-8129-b8a9610f1525 | -8.94713 | -47.61245 | 2026-07-15 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0984c40-1968-3362-bee6-f0094fca1387 | -8.50979 | -48.07236 | 2026-07-15 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20c28be3-d4fd-3014-8e70-be0f7f5fb773 | -8.50639 | -48.07181 | 2026-07-15 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb4e5527-b44e-3d97-82d0-1580187cc072 | -8.74156 | -49.44799 | 2026-07-15 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68c8816a-a3ee-3185-a8a5-bde8a64cbd12 | -9.88342 | -49.97874 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b87f79c4-bfa2-31f4-955e-ba34bfcbe777 | -10.74238 | -43.61363 | 2026-07-15 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 58d0bda8-6c6d-34b8-b5ce-f6d34219f940 | -11.87247 | -43.79633 | 2026-07-15 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a687a5c0-1950-3ea0-b839-595e224d69ec | -11.86732 | -43.80034 | 2026-07-15 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8007d6d-2e00-334c-bbc3-37b2e2e9e6e3 | -9.40464 | -48.93937 | 2026-07-15 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ea11dbf-55f7-318e-b8f4-5ba2844e7744 | -7.46509 | -49.56223 | 2026-07-15 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07d9a9a7-7aaa-3c4f-8a37-0cdfd1c8cb32 | -10.74179 | -43.61813 | 2026-07-15 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 839ae2e6-52a0-324a-b3ec-717ade0c3764 | -8.47354 | -51.57326 | 2026-07-15 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94665a9f-68e6-3ecf-9e54-2154591797ff | -9.18837 | -50.87521 | 2026-07-15 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 982d1e84-7fa5-3944-9cee-a064ad51cc5f | -8.73178 | -47.83057 | 2026-07-15 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70936b56-8bb0-3e03-95ea-78159676a69c | -9.75535 | -48.55324 | 2026-07-15 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03057a2e-4b1d-36c8-b035-a08d055c317a | -11.42775 | -47.52736 | 2026-07-15 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bb2dcf4-2815-37c4-a99b-5c13947c9892 | -12.35978 | -47.41327 | 2026-07-15 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15e2b003-9752-3d69-9a50-528c750a4844 | -8.50355 | -48.06757 | 2026-07-15 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33a5e99f-db01-3af2-a60a-1ea7370a3ba3 | -12.66234 | -48.23445 | 2026-07-15 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9048a4f7-5e7d-3581-af61-b70fdedc5b10 | -9.54487 | -49.30945 | 2026-07-15 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6430142-f53e-33d1-96e0-1b9bfb36e9d0 | -9.87957 | -49.9817 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 529611a0-335d-3fc1-94d4-25bc54643419 | -11.43071 | -47.53214 | 2026-07-15 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe7c2a70-3194-3073-bd58-4cff584c2db3 | -9.74467 | -49.0463 | 2026-07-15 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 48b4f801-356f-396f-8fd1-fe2ca3c640f8 | -12.66175 | -48.23843 | 2026-07-15 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18bdf9e4-dfcf-3da4-a4dd-1e3336f0fa65 | -8.45176 | -51.5505 | 2026-07-15 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23833ad8-8866-3c77-be23-eb0e482a43ab | -13.2734 | -45.17574 | 2026-07-15 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14823599-0561-3041-9978-1dc12633b6ee | -11.45016 | -45.12654 | 2026-07-15 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53a0ca24-2a7f-3ee9-93b8-6f19e3a6139e | -10.78861 | -56.74122 | 2026-07-15 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0d57ec85-b5e2-378e-9273-6500b97fe592 | -10.09664 | -50.13787 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51ba91e1-0438-36ca-b069-8668ea2ac0f0 | -8.48031 | -51.5744 | 2026-07-15 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04a4c904-84f3-35d0-a88a-29bd6f07c7ca | -9.74521 | -49.04273 | 2026-07-15 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 342d92a0-2d01-3d8f-8803-706257dc5912 | -13.27024 | -45.16723 | 2026-07-15 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fcb1fd7-e852-3bb8-bf8c-49477900b9e0 | -10.10048 | -50.13491 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61f69a39-6265-3390-8d41-45b9f64df114 | -10.7469 | -43.61418 | 2026-07-15 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e6670b49-da6e-35d5-9e1e-b04fba50d892 | -8.50807 | -48.0607 | 2026-07-15 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90ae862c-e138-37f7-9720-b5a1d55454ce | -8.74825 | -49.47044 | 2026-07-15 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b0764cdc-3820-3a66-b80a-a34b8f27153e | -10.26186 | -45.63896 | 2026-07-15 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cc7b3d9-d21d-3df0-ad84-c5df65c65f63 | -9.54921 | -59.30983 | 2026-07-15 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e794dfeb-0e6f-382d-8bbf-e2a26d444472 | -8.72834 | -47.83006 | 2026-07-15 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 773d717d-9f6d-3087-b607-e5340bb0667d | -12.66643 | -48.23103 | 2026-07-15 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13c8d9bc-dcd9-3df1-9c6a-32e979e1e133 | -12.65942 | -48.22992 | 2026-07-15 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c97af76-584f-3f7b-a666-0b66cc65355b | -13.27392 | -45.17181 | 2026-07-15 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 122b6f99-1bcf-37ac-87f8-bf2cef005d6b | -8.89867 | -50.16325 | 2026-07-15 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0a3ddd9-0a1f-3d31-a905-4511c070ffe7 | -9.74187 | -49.0422 | 2026-07-15 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 242dfe0a-a10d-30ee-8a23-cce06da1ddc6 | -13.4414 | -43.84742 | 2026-07-15 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d3bea9e2-1c99-3f38-b98c-af85f25a6b86 | -10.23849 | -58.51886 | 2026-07-15 04:40:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff91e5fd-aaf4-3507-af70-9a51e74045b4 | -10.88168 | -49.54739 | 2026-07-15 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afa1fa57-bd54-35e7-9a7c-38172225d84f | -9.73853 | -49.04168 | 2026-07-15 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f42d928-b9e0-362d-b859-a7b80358856c | -13.44078 | -43.85228 | 2026-07-15 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8a563444-7043-352d-b400-3cfb219de267 | -9.88672 | -49.97926 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1de36fe-f2be-3cb2-ba43-77227295f20c | -9.88288 | -49.98222 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b99b42e-d144-3ca0-a0e9-a54b2685585d | -13.44599 | -43.84827 | 2026-07-15 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 881659c4-76dd-328e-b443-69466f56a00b | -11.42838 | -47.52306 | 2026-07-15 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 034bab62-ddba-33f6-a1b7-60632359aacb | -8.07486 | -50.0604 | 2026-07-15 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4d9664f-8900-3657-b81f-d76b4600e34c | -10.78938 | -56.73692 | 2026-07-15 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 022ebaeb-b5cd-378b-b6b7-5e2c3903c375 | -11.44553 | -45.12971 | 2026-07-15 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ca30f81-3ae0-3d53-899f-55d3e803934a | -9.74133 | -49.04578 | 2026-07-15 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8fef5850-306f-3a77-b1f7-2b0e1aa67103 | -11.57588 | -48.39956 | 2026-07-15 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9581495-1aea-3f6a-a960-f514bd1324d1 | -11.44965 | -45.13028 | 2026-07-15 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9671f1b0-390b-3773-8d2d-48d15a1b904f | -8.94771 | -47.60859 | 2026-07-15 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a997ca1-d64c-30b8-b916-91890e152b70 | -12.43702 | -49.57742 | 2026-07-15 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13173dd2-00b8-3e96-805b-33eacd720dc6 | -9.74801 | -49.04682 | 2026-07-15 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7fc4554-2e08-3999-973f-00455506bbab | -10.71569 | -45.15076 | 2026-07-15 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f37d207c-4049-30bc-b76e-7df83503b3eb | -8.85546 | -50.02849 | 2026-07-15 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d373acc-ba67-371b-b706-a24269ad10b9 | -8.50924 | -48.07605 | 2026-07-15 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 310de160-2ce4-3583-9f3f-3bc832bc6519 | -8.50584 | -48.07549 | 2026-07-15 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d146882f-e346-3bad-b19b-468f1a5217b7 | -12.66292 | -48.23046 | 2026-07-15 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d77498-52dd-3dab-982f-23aef9521bd4 | -9.15672 | -48.95907 | 2026-07-15 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3899300c-b288-34c0-9bfd-a4569d84c935 | -7.4634 | -49.55135 | 2026-07-15 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 155f419f-ec3c-3b5d-8f43-f2e6cb40ebb5 | -13.27445 | -45.16788 | 2026-07-15 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a509481-d42a-3c6d-94e2-b7d5a30d8c00 | -5.90015 | -46.20832 | 2026-07-15 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2509a42d-8217-3319-8ae6-1253c0cdc6b8 | -9.18505 | -50.87467 | 2026-07-15 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5b73cdf-3e1c-3bb9-b0ff-9063dacbce23 | -11.43431 | -47.53247 | 2026-07-15 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90e37e47-00ce-347a-8e23-8ef9b7a40a2c | -13.2776 | -45.1764 | 2026-07-15 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4220aeeb-df12-3eca-8a22-3d286eaa4849 | -9.54542 | -49.30593 | 2026-07-15 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cbd77ad-1bf1-3e33-9aae-f2cfc5cf68b7 | -8.83073 | -48.33501 | 2026-07-15 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5f6f734-5272-3661-bd23-780749479667 | -12.44875 | -49.59039 | 2026-07-15 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7735b19e-28bc-33e5-a670-22073301a7a0 | -11.55551 | -52.78277 | 2026-07-15 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e408fef-4423-3b9b-b79f-0de2cf7cce36 | -10.07574 | -50.1417 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c3cf7e5-17c9-3790-a80b-92926419a6d9 | -10.45781 | -55.06519 | 2026-07-15 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffa3e095-fc12-3816-8307-c6bc5bb819de | -5.62759 | -49.19469 | 2026-07-15 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0356cee9-8e4c-3b54-8382-03d08786dff9 | -12.44596 | -49.58625 | 2026-07-15 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f58085af-78c2-3771-bd32-edba76c0a414 | -12.36074 | -47.41152 | 2026-07-15 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edd30798-7cba-3e8b-85d8-e5a50c0a33a9 | -8.50299 | -48.07126 | 2026-07-15 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1b130e7-4038-3b72-a2f4-362a26e9d3a2 | -8.75155 | -49.47096 | 2026-07-15 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README5.md)
