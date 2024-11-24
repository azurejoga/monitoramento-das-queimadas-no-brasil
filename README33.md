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
| d43902d3-f74e-3d7e-a0e1-237d208c9f4e | 0.4058 | -50.86159 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8a5bd19f-b642-333c-a301-956d8664a7f3 | -1.81489 | -46.63617 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aebaaffd-1773-37d7-ad35-1fb56794caff | -2.79686 | -48.68354 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 988831cd-a6d7-377a-8b9f-c28e9af924e4 | -2.27558 | -47.98063 | 2024-11-24 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a005dc62-6ce8-36fb-b9be-4f50138c4c1c | -3.98657 | -44.79503 | 2024-11-24 03:57:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7511559a-0cb2-3bcf-80c5-31b0cfd50035 | -3.62857 | -52.25705 | 2024-11-24 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbb7d2c5-1474-32a2-b325-deccd59f3238 | -4.23701 | -48.67527 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 077da6b5-05cc-3c7c-81bb-02112e1a5380 | 0.41464 | -50.85948 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 04da62d7-f70b-3ba4-8f4e-fca26a45d3ca | -7.14221 | -38.70517 | 2024-11-24 03:57:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 26bc652d-c99d-3b11-8a9e-52d2f808dcc6 | -4.41313 | -44.099 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b58e2865-c910-3c6c-9d45-5d4fb1a0d472 | -1.74889 | -46.70322 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 081acca8-a729-397f-9d02-8b66ee461bb2 | -4.26469 | -49.8303 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4d330fc-da76-38d8-8249-7f6fa578f24c | -4.69553 | -45.70173 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0534b2b-fc5e-3050-9141-7fe3ffc66123 | -4.42543 | -43.46658 | 2024-11-24 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c86b935-b9f8-3e71-ac46-0969bd0a236b | -6.34248 | -39.61425 | 2024-11-24 03:57:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e927930b-346e-3461-a302-27e2cf27d3c4 | -5.00243 | -42.94574 | 2024-11-24 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5b23b50-6a7d-3b14-80de-370eadb3fd41 | -3.38378 | -50.32734 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 238e5abc-5957-3c47-96f0-e5c8d21ca086 | -2.21234 | -46.38872 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c6167b98-acc7-3709-a4fa-4de02dfaa07e | -4.35485 | -45.87782 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f51a8e2-d7a2-38cc-a1b0-c7bef0f2c4b5 | -2.75348 | -48.67295 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a4831c2-8829-3a99-b2b0-b356aa35e49f | -3.54332 | -51.52253 | 2024-11-24 03:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16010e42-ec9f-31f4-a563-c2edf4414548 | -3.29191 | -45.73031 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a8ceced1-8322-32ff-9895-5cff13cda423 | -3.04173 | -49.44822 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 19c3c228-b949-378e-a2c6-cceecd9d3f99 | -2.85889 | -48.44018 | 2024-11-24 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e3f72e5f-633c-3339-84b5-a7218f3025a9 | -5.38718 | -44.21152 | 2024-11-24 03:57:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e036988-ab84-38ce-921f-785c97b7857c | -3.46978 | -50.01345 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26c5cd3f-3a93-3347-ba7a-4ddc145b7414 | -0.87532 | -51.72619 | 2024-11-24 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a7b6b56-0a7e-3995-b79d-fd0c7cec95f4 | -2.70535 | -46.28889 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 399d4818-e22a-3b26-9199-37412e3367cd | 0.42034 | -50.85266 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a6681cb-9c14-32f2-bce5-f2f2988cc601 | -4.31291 | -43.20303 | 2024-11-24 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97d396b8-d7d9-33bc-8ee9-80b5c96d55df | -4.41744 | -40.84916 | 2024-11-24 03:57:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b2d2cf2-ed24-3090-9a6f-6bf4f4099599 | -4.75812 | -44.39596 | 2024-11-24 03:57:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0397b835-ebf1-39e7-82d1-176bcb7ff5bc | 0.41904 | -50.85934 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19e6baaa-ce8f-364a-9025-d6bb717efe43 | -2.24572 | -46.87015 | 2024-11-24 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef69c4cf-1a9b-3774-a586-7a63433cc895 | -2.5778 | -51.89488 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0f35176-999b-313f-bb19-981f79971ce6 | -2.7398 | -49.11985 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6de4fc96-4645-3516-8d0e-876de9395adc | -4.70171 | -45.69754 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8ca216-4da5-3d30-89de-af2df8d8d504 | -2.66811 | -46.60567 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca1ef2b0-5173-39da-baa9-38b8fb200019 | -3.49902 | -50.46703 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 772a118f-84d4-33c6-a584-2f4410ef30e9 | -0.57731 | -51.73242 | 2024-11-24 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8787bcbc-eba9-3e0b-9a88-57eecdd1f3ca | -3.29637 | -46.15332 | 2024-11-24 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48837c2a-3f20-3952-9b06-08694fa37e0e | -6.3013 | -44.88156 | 2024-11-24 03:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 855f514d-0ab8-393e-9086-05e97eef269e | -5.37443 | -43.42487 | 2024-11-24 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c83bedbb-04f1-3234-9078-42280782b018 | -5.07033 | -42.57118 | 2024-11-24 03:57:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04544808-9ef5-3b40-a1f5-2249f384116d | -5.35799 | -45.03837 | 2024-11-24 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9514259d-c9e8-3527-935d-4a627d361ffa | -3.11242 | -44.0975 | 2024-11-24 03:57:00 | NOAA-20 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f1f2b73-e50d-304b-afff-6ce95f1ce5a1 | -4.51173 | -45.80572 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea9212f9-1c04-3a62-b461-b1b0ea404365 | -4.08199 | -46.15426 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28519c90-ca2f-3b79-bcde-6343a44a3805 | -6.57699 | -42.39719 | 2024-11-24 03:57:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bf4ee9ed-b38d-3586-8ccc-5ec6c640d648 | -1.83602 | -46.64654 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3cbd547e-eb30-3c8d-a0ea-c0912d76e9d3 | -4.88736 | -48.90967 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fba3a84-26ea-3cb0-98cd-d5bbae767364 | -3.85513 | -50.05498 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c2a5f3-ef92-3f2f-8db7-fab792e79ca4 | -4.19 | -42.96275 | 2024-11-24 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc87a905-f5ad-3925-8ba1-343a7be96be8 | -3.09586 | -49.02444 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec813f93-67a3-3f99-ae35-3f858070bb2e | 0.41555 | -50.86522 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 725c7d93-1821-3000-8580-6173c0485155 | -2.21709 | -46.38952 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7c48e2ba-b143-3b49-bb8a-d565a91f8b81 | -5.19159 | -49.15512 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 415172bd-d02b-38bb-8a91-d393ea103d0b | -4.31906 | -38.12989 | 2024-11-24 03:57:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 928d729d-60b9-3719-9e7f-64fa7e110575 | -2.59241 | -46.85445 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fca96f0-f19b-3976-bde7-abcbf91ed2a7 | -2.32304 | -46.34715 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41e701bd-b3b1-31bc-9099-5750c535aabb | -2.28496 | -47.31325 | 2024-11-24 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a09b042-fbf9-3a30-8cfa-7b5c07cff9fb | -3.83777 | -44.05209 | 2024-11-24 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ffa6ae9-6900-3c19-9239-7706e388a996 | -2.45275 | -49.08521 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f5ed10d-481a-3e41-832f-54d90760a9df | -5.19726 | -45.41205 | 2024-11-24 03:57:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef42aebf-7e25-3b22-8235-487803738ccf | -3.63914 | -50.2281 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aac02895-be83-35c4-a7e6-624ea13543d5 | -2.00286 | -46.28762 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 634103eb-e3e2-3acf-a532-6f9428dc624b | -7.14166 | -38.70877 | 2024-11-24 03:57:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e755ee4e-336d-3bcb-a225-56f48a4ddc9e | -4.23081 | -44.63284 | 2024-11-24 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 633436e5-45f2-392e-91cb-3d1dd5d2537e | -3.44042 | -50.02402 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bd8230f-75e8-3b06-8b2a-ae90424c590f | -4.55085 | -44.0163 | 2024-11-24 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0c2de6d-222e-3e63-8b13-3061c949298f | -3.85689 | -50.05964 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e660d331-fc11-3339-8dbc-d7b1998e2462 | -1.34935 | -46.91587 | 2024-11-24 03:57:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 733c92f0-04b7-34d2-91fc-755b7d171a3b | -4.62565 | -46.04591 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4c68712-609c-33e4-97a1-1a4e083a879d | -3.10384 | -45.78064 | 2024-11-24 03:57:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 46686a92-2244-3b0c-a6d3-5f7d9d757b9a | -5.19998 | -46.1398 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1511bea5-ca49-3b3a-94e2-788ddf3a9107 | -3.70189 | -47.12788 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b7e32e-fefd-37c9-b45b-da4b24954951 | -2.68092 | -46.15636 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93420aed-f980-3f3d-bdc2-5defd396bee6 | -3.13337 | -45.38067 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4abb5756-c16c-35e2-af4c-c41260ef7695 | -3.12268 | -45.27991 | 2024-11-24 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f6ad0bfc-8702-3269-a279-11ad6d4b1630 | -4.18041 | -45.62777 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b18cf5fe-757d-3ded-bb63-01592b1c4e5f | -4.84887 | -49.36138 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f165bc7-7fe7-3bc2-b0b0-87b8664f4768 | -4.53956 | -42.91175 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b36a749b-0baa-3608-9250-16f8e5e6cfa9 | -2.65075 | -46.13651 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3725f696-3776-3a2d-9499-d4b6c4b68b26 | -5.19029 | -49.15785 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45506124-605a-3529-889e-0483174ef0a5 | -1.81976 | -46.63694 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fef288ca-fa2d-347f-b723-e4f2666cf523 | -1.82692 | -46.65471 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddd25fee-87e7-388d-b2c5-e272892d7306 | -1.9631 | -48.38884 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3abf47f7-9177-3fe7-9537-2d4ce76846a4 | -3.16979 | -45.299 | 2024-11-24 03:57:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ce31cc4-62f0-3aff-81c6-e4af057fc20b | -5.41243 | -45.76233 | 2024-11-24 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbe93c58-c9e2-32a2-b948-868d8640d48a | -3.52989 | -50.75918 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cfa8172-bece-391c-b30c-c5cf51df1b0a | -4.23142 | -44.62923 | 2024-11-24 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8988e234-0010-337d-972d-477827be768c | -4.81969 | -48.5141 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 477df973-1146-3f7c-ac5e-78bb755c5e6e | -4.55074 | -44.01877 | 2024-11-24 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f7469d85-230b-3ea6-b5d3-640b1cf9fc89 | -2.28143 | -47.31095 | 2024-11-24 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d73d0ac-1983-3831-873c-c6518d3518c6 | -2.6554 | -46.13724 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0c362d2-0bf5-3820-81a6-56ba3adda259 | -2.75288 | -48.67657 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9de711db-bd07-3d4f-9380-7922e408aaf3 | -4.70764 | -45.43845 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3444f259-d9da-3bc8-8bd8-cbb503565938 | -4.24196 | -48.7111 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e66dd57-1bfe-36e2-b870-3e7d7f29539a | -3.98452 | -44.79479 | 2024-11-24 03:57:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0787f5a3-bcac-3d86-9698-8efa80d854f9 | -3.8576 | -50.0554 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README34.md)
