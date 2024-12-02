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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7203eb8b-ed60-30ec-b82e-0f8e9eb5c462 | -9.99271 | -44.74282 | 2024-12-02 04:04:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3956ba94-635e-375a-a781-a82dbd623ada | -10.66028 | -44.49483 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7ae1c18-958a-307e-85ef-cec569440810 | -10.65957 | -44.4991 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8aba72ff-217f-37d8-85fb-c10a16559fa5 | -13.74341 | -43.62742 | 2024-12-02 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49f28e08-0718-371a-8947-36d11b672289 | -9.33544 | -36.01505 | 2024-12-02 04:04:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 4748953a-3dfd-3950-88db-591c0526cea3 | -11.06105 | -45.3772 | 2024-12-02 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce8c1a22-04dc-342c-8054-157255b3802e | -9.37794 | -40.67646 | 2024-12-02 04:04:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 184a071f-644e-3dd1-ac8a-9974a5fd98ca | -10.66098 | -44.49056 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b256029-0a9e-3514-9f02-f289a79a5967 | -9.33617 | -36.0099 | 2024-12-02 04:04:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 594402eb-1504-33bc-9a90-9b68507f471e | -11.28065 | -41.7303 | 2024-12-02 04:04:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 998f00fb-9e80-34aa-a519-425cdc785ff1 | -9.97467 | -36.33739 | 2024-12-02 04:04:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b5b46aae-4c47-30c6-9470-c653b7a7b3d4 | -9.88929 | -36.17819 | 2024-12-02 04:04:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 6b21e521-a757-36de-8ef8-30ad82630280 | -11.63316 | -40.15261 | 2024-12-02 04:04:00 | NOAA-21 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 825237c4-1aae-3fb0-8e3e-c9995528413b | -9.18702 | -35.73986 | 2024-12-02 04:04:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3497a58d-ec68-3797-8c49-e0db79ed9188 | -9.99118 | -44.74081 | 2024-12-02 04:04:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdb2c690-8a96-3d59-bd44-9a871b6cd7cd | -9.77652 | -36.15446 | 2024-12-02 04:04:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1e59c07-1e75-3020-b77b-79b38f6e6b9d | -9.33941 | -36.01561 | 2024-12-02 04:04:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 43ad7f21-3159-396c-ae9a-f125a0e77b3d | -9.33147 | -36.01449 | 2024-12-02 04:04:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 17f409e9-f65d-3ecd-a6fd-7ea7c805d6a0 | -10.5009 | -44.91356 | 2024-12-02 04:04:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50738625-10a0-38aa-aeff-5f533f83e152 | -12.51369 | -38.30428 | 2024-12-02 04:04:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 133a3cde-8a0e-395a-90fc-c0edf690779f | -17.39571 | -42.65682 | 2024-12-02 04:06:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d068c841-035f-32dd-bf99-18dc35623a17 | -20.32561 | -48.8236 | 2024-12-02 04:06:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 138a54c2-d779-3971-93f9-b294718aaade | -17.59649 | -43.19773 | 2024-12-02 04:06:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f313413-dbc8-3846-b562-3917360d25cd | -17.09466 | -43.80455 | 2024-12-02 04:06:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 770ed671-0a41-387c-a156-634123eefb30 | -20.377 | -45.60351 | 2024-12-02 04:06:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8615eff-dd66-30f3-b47b-b3f2af334363 | -17.61715 | -45.00915 | 2024-12-02 04:06:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb629216-31d4-33b5-8b5e-ab28a192db02 | -16.34985 | -43.69565 | 2024-12-02 04:06:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c11bd70-bda6-39e4-bcb8-83c73cfabc01 | -16.68233 | -43.88524 | 2024-12-02 04:06:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1748869d-3562-3800-99ca-cf66ce42b63d | -16.04814 | -46.20102 | 2024-12-02 04:06:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af7f4050-e1da-382f-b0ee-23209ce576e0 | -20.76289 | -46.77104 | 2024-12-02 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7197f1f2-d262-3554-9486-1257b4089a82 | -21.18041 | -43.97863 | 2024-12-02 04:06:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30d469ab-73ea-3bb1-9362-8d5c3959504f | -17.77968 | -42.81066 | 2024-12-02 04:06:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2abcd0a2-dca0-36eb-9f9d-f0a9ef263f22 | -20.3249 | -48.82739 | 2024-12-02 04:06:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6212dde6-b40f-35cd-85a1-936d45eb55ec | -19.16619 | -40.14384 | 2024-12-02 04:06:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5f5a2ec0-258c-3be9-9f70-c98d1083d6df | -15.56777 | -47.85524 | 2024-12-02 04:06:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18b70ba1-c3f8-3835-83d4-cfdf985cb3d7 | -20.41759 | -43.55347 | 2024-12-02 04:06:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| de175988-1c8c-3444-a741-5e35f58344df | -20.33363 | -48.82542 | 2024-12-02 04:06:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1541fc5-c4d7-358f-a62d-edd83a7af4de | -16.20803 | -43.89912 | 2024-12-02 04:06:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd9fe68a-1c10-3174-8893-6c5de8d207d5 | -16.5808 | -43.61401 | 2024-12-02 04:06:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48f81328-2ced-3419-8d48-b5038d236b19 | -20.89944 | -43.81924 | 2024-12-02 04:06:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 509f6282-aa87-3981-bcdc-19c3292a0a14 | -17.38521 | -42.65874 | 2024-12-02 04:06:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 371c9794-435d-36b5-9867-294d83f2a565 | -20.76488 | -46.76982 | 2024-12-02 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 76c6de38-d11a-3d6b-9f96-b6b75a3e61b7 | -19.72853 | -49.63686 | 2024-12-02 04:06:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a6ed91d2-56d2-38ce-8cf4-c797bd6ef5e6 | -20.32962 | -48.82449 | 2024-12-02 04:06:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54c3afab-ca52-3035-8819-2ddcc86e2906 | -17.50149 | -45.17599 | 2024-12-02 04:06:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b9028e0-fb4b-3528-9ff4-8fcd73a3755d | -20.72339 | -54.42501 | 2024-12-02 04:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9a7b365e-b6b5-355f-8536-3c661a2c6e36 | -22.83731 | -43.77462 | 2024-12-02 04:08:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86c143ac-980c-319c-9400-d0a7533ed355 | -23.59353 | -47.43822 | 2024-12-02 04:08:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3e0bcc58-cd8e-3caa-a1e5-f312b1fdba98 | -22.55223 | -43.55232 | 2024-12-02 04:08:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 553f2f2f-2536-32e0-9c53-680f36c547a5 | -22.55612 | -43.54922 | 2024-12-02 04:08:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 24d14c1b-089a-3e6e-b7ec-ead2893f353d | -20.72161 | -54.43299 | 2024-12-02 04:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 239eed95-91f4-3fe7-a4e6-ee7738c29d4c | -22.26488 | -46.1545 | 2024-12-02 04:08:00 | NOAA-21 | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d794d4f-dd3c-3cdb-9429-fc0e15c9e58d | -22.55555 | -43.55292 | 2024-12-02 04:08:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a026af2c-6e28-3f8e-973b-f7fe5da19ddc | -22.85592 | -42.98139 | 2024-12-02 04:08:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8c8f911-d7fd-3483-a939-fdf1a0ae0492 | -20.7225 | -54.42901 | 2024-12-02 04:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d09b818b-dc95-36a2-b594-864a7f637c3f | -20.72811 | -54.43046 | 2024-12-02 04:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7356051b-f4c5-3bd1-aab0-1788fe57755d | -20.72899 | -54.42648 | 2024-12-02 04:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6d72a880-e9d0-3a52-a870-9f1b06470ef7 | -22.51911 | -47.8928 | 2024-12-02 04:08:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75816a22-1965-397a-bb77-7e4072284a72 | -22.71876 | -48.23746 | 2024-12-02 04:08:00 | NOAA-21 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 408b9719-5b36-3e14-b895-50a3a7939840 | -3.259 | -53.6388 | 2024-12-02 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 19bc481f-2f2a-372a-ac9b-2f4aea05f730 | -5.5882 | -45.1412 | 2024-12-02 04:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1fbc1753-0f35-3ba1-8a91-c7785b0c3b6e | -5.1369 | -43.1951 | 2024-12-02 04:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 355aa8f0-215b-3de0-b212-2a07f8e33731 | -5.118 | -43.2198 | 2024-12-02 04:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 2957b0f2-2e26-38e5-abd7-8c8be32cc757 | -5.1367 | -43.2185 | 2024-12-02 04:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e469f825-7edc-375d-ba4b-32e1154c3a9b | -12.4358 | -63.7455 | 2024-12-02 04:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 43dcbe73-42b1-3f0a-96f1-80ed6651370c | -3.2708 | -46.4511 | 2024-12-02 04:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8999b0e3-ec38-3d89-8376-521a54c88bca | -6.086 | -48.0557 | 2024-12-02 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| bea73559-b4b9-3a1d-aac0-28bf803789a7 | -3.2591 | -53.6186 | 2024-12-02 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d1878f4f-133e-348f-8596-c6ed1e72aa34 | -5.1367 | -43.2185 | 2024-12-02 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0781c7a6-9907-3972-a801-13fbbedc6dc6 | -3.2708 | -46.4511 | 2024-12-02 04:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cd4f3c3d-69a9-36bf-8190-386acbb2c85b | -5.118 | -43.2198 | 2024-12-02 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 68ec742b-5f59-3380-9853-39a021e4a3ab | -12.4358 | -63.7455 | 2024-12-02 04:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 42eaecc9-5cc5-3ddb-b85a-63226a76cd57 | -5.1369 | -43.1951 | 2024-12-02 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a8ff2517-2e22-39d1-a98e-5ab2e11b6789 | -5.5882 | -45.1412 | 2024-12-02 04:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0c4c89bc-238a-3825-ab93-fb8cd1c4a71f | -3.2591 | -53.6186 | 2024-12-02 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c4ccb840-41a8-3e22-8cba-cc0e22feb8c8 | -3.259 | -53.6388 | 2024-12-02 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 5c952d5b-1a95-3b4c-963b-ba7c4f32ea7c | -5.1181 | -43.1964 | 2024-12-02 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 097a10d2-9d34-304c-acc9-6682cb6ea615 | -1.95 | -51.20726 | 2024-12-02 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2f45ce8-0e71-35ce-a2e1-0b8186af6205 | -1.13997 | -53.67297 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bdbadcd-193c-334d-98bb-0fe27662d635 | -3.04929 | -48.52941 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a8ea3ff-2bb5-305b-bfa0-20cfc5345c31 | -1.94694 | -53.34475 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42c6353f-7598-3468-8f6b-5ab1c69ee8b2 | -2.58942 | -47.0381 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 633ea3cd-0f4b-34d9-884c-66396f36125a | -2.46731 | -46.57289 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e93bbe12-86e0-3a7f-96dc-b8efd9fdda87 | -3.17364 | -46.32236 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d572e9-5b86-3828-a801-74d231f12b3d | -2.83746 | -46.86123 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37dc8913-2c13-375f-a15f-e867927ea9b2 | -1.73253 | -52.63357 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1f8564ed-47d2-354f-a74a-71748ab259f3 | -1.8146 | -46.63655 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b40446bd-2710-36ef-97b5-d7961f7b7e7a | -2.63508 | -46.88168 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8358793-bd87-38c7-a3a9-986e301b2ba3 | -2.62251 | -46.96127 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fab10cff-1370-3484-97dc-b56ac0e7809d | -4.11021 | -39.99254 | 2024-12-02 04:23:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4abe14d-037a-324c-8353-3e098a9af7c1 | -2.1955 | -53.77412 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc7459c7-d8af-3a81-8465-f6c4d3d55816 | -2.285 | -45.60334 | 2024-12-02 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a31fdd1-2b17-36e0-830e-dcee1470045d | -2.66326 | -48.79988 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4984d77-bd88-3916-86ae-d84132a8b417 | -1.49708 | -51.93645 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6704af8a-68e2-3f07-8f91-f4a13c4bb113 | -2.01807 | -54.3145 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69fea53d-25c9-3a42-865c-62ef896a9c58 | -2.56266 | -46.34904 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76e8c3ef-87de-33c5-aa9a-839481547140 | -1.63137 | -45.41232 | 2024-12-02 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93e671b8-3721-37fd-9ae9-f4ec038214be | -3.27152 | -46.45232 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 812751ac-f7c7-3208-998d-e78ae6e18de9 | 0.89099 | -50.95926 | 2024-12-02 04:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcc1da78-f6f1-33e7-a40a-7752454a9bac | -1.47044 | -52.68624 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README28.md)
