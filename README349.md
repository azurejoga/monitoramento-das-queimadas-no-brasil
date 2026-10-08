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

## Dados Diários - Página 349

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a220e16-8760-3733-ae98-0a3583219f76 | -5.28808 | -42.72862 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 3b97cc62-05c9-3c5f-8f2c-f3db41595db5 | -2.46423 | -56.08761 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0bf94ff6-d980-3f9e-a84d-663317975646 | -5.3562 | -45.92929 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b9617963-6f01-3202-9166-cd273be18b86 | -3.04288 | -54.27679 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 14fc135e-34ad-3f2c-a348-1ed348f91c5f | -3.30489 | -53.69223 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 6cbc8618-b650-3244-bab3-4b8bc3125765 | -4.35889 | -43.79836 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf0b0ad9-6b34-34af-91ac-5c667c788c6e | -6.12382 | -53.05482 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 191ba42c-c81e-399a-9e26-dcd44f6b5923 | -0.0839 | -49.48166 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 71bf77d5-1f7b-323c-8209-9412a13a12ce | -2.54849 | -57.38481 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00dd32c0-7d01-3751-b2a0-ef3c34fb222f | -5.7062 | -53.46273 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| ad8e47e1-3074-3a6a-8956-c63d945898ba | -4.6303 | -43.49629 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4ecee39b-995a-3062-91ec-ae29486ba966 | -2.97358 | -54.10769 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62a194e8-e215-377c-bd43-231c9d92b8ef | -2.84482 | -54.12965 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fb7e57da-3fd6-391e-a89d-6c26d7ad6d05 | -5.28744 | -48.10349 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| a688640a-4f2a-3d7d-b1c9-f80433ff6493 | -5.37765 | -44.2004 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 31b6dd4e-e855-3a48-a830-49471dbbc5e4 | -6.72628 | -55.06205 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 31186316-173d-3e56-bc87-22ceeea87eeb | -2.5782 | -56.16857 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d604385a-75be-3ace-8f49-0e1764bd5f88 | -3.10643 | -53.77555 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 25f6db92-d2e9-3076-bba9-72abd402a4e6 | -7.23802 | -55.11538 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6e31365d-24b4-31b8-9f93-817129caf1ff | -4.01305 | -41.77394 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 6260843b-66a6-3e5c-be3e-446a0d97e736 | -3.40627 | -42.8055 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f148c4a1-e793-3563-aab3-f033d0224137 | -3.10265 | -59.19353 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ffb96f6d-4c29-32eb-9e62-a20509eb869b | -3.29057 | -53.71638 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5f5e2ff7-d7ea-3b4a-964c-3b9c240f000b | -3.28833 | -53.70168 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1a905bdf-54ad-3184-8489-b301b9cee199 | -3.10263 | -54.286 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e3102115-c964-3f44-bfc6-bd6e90f262ca | -1.1083 | -54.16943 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a567102f-a96c-34df-bff9-53aa194368cf | -2.66203 | -47.89291 | 2026-10-08 16:39:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6d2644cc-94d7-382c-8396-fddd76cb4a57 | -7.50907 | -55.57285 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a48296ed-7a87-3001-baa9-1ff55ec97b1c | -5.67846 | -43.4181 | 2026-10-08 16:39:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d2a9e34f-7c51-385f-a4b4-444e4a04dabb | -6.15394 | -47.93178 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4bc04e5e-4479-34c9-a25e-55092e01522d | -2.57384 | -56.17636 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| cf81fc3a-d61e-3781-a443-8c9dcc00fcf9 | -3.00856 | -43.10736 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bcf5e08a-ee4e-3a10-abd9-f1d178ed550a | -6.71092 | -56.1448 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4cee87bc-21f1-3403-bc24-9d6836481b15 | -3.09966 | -53.76165 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 30115970-a48e-342a-9a38-e4dee59575cf | -3.76667 | -44.36252 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 630bb964-cec0-34de-9910-1c301ed2a255 | -5.30738 | -45.72095 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f84b9850-1808-315d-a735-46d1f0476cd8 | -3.87531 | -42.83393 | 2026-10-08 16:39:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a0591f27-e3d4-3454-afc8-6d5a258c283a | -5.9128 | -53.88919 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d540a8b1-b81e-340d-a206-8a9391a052a2 | -2.7843 | -57.64353 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 685b2da2-3f8a-393f-8a31-f5e31130cab3 | -6.78181 | -56.23058 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| d34ddbda-7311-38df-8926-d990b02a05c7 | -6.07731 | -59.88371 | 2026-10-08 16:39:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 19fc7bc7-ea5f-3575-ad52-18e841a4b44d | -7.50958 | -55.57652 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 50d0adbf-4356-3847-9924-469dfdfa02f4 | -4.35758 | -55.22854 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8833d05a-74d4-3bb8-be30-4e156d7f18d1 | -2.61361 | -56.47817 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7e55acea-4bbc-36f5-8bcc-7e0bc5760046 | -2.84775 | -57.47571 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 6b748ca3-fc3f-33b5-bc28-2c63d51f8721 | -6.39162 | -52.727 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bd527e80-ff33-329b-afe3-dcbb5dfdfa32 | -1.62469 | -55.12443 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0670ac51-e417-33fe-96a4-f502172fcd51 | -3.00504 | -42.86711 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2c9414f-c963-3173-a2a4-75e58725c8a0 | -5.4859 | -45.22781 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4ba5313b-546d-3871-92e5-ccf78725ff3d | -4.19343 | -38.74141 | 2026-10-08 16:39:00 | NOAA-20 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 7d6df159-188d-3f1a-b062-7204d8bc498a | -6.10189 | -53.45903 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ab5ba131-e28b-319d-9904-c697cb5464d4 | -3.40583 | -46.73607 | 2026-10-08 16:39:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ffd426d1-1c8e-383b-9a92-a90a6ada1394 | -4.09119 | -44.10242 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 28ed0369-8f1d-34c2-b5f3-daba4ac9a767 | -5.89237 | -44.17609 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 399ab4f0-cd80-3dcb-8948-22146669036e | -2.55713 | -57.43359 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6e93ad86-0ede-39d7-b939-034d7d18127b | -2.48075 | -56.10899 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fb039424-4c7d-30a0-b778-1c4984e88b17 | -2.36958 | -44.43277 | 2026-10-08 16:39:00 | NOAA-20 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ef152c8d-5f6c-3d70-b5ce-d63bb4b1f739 | -3.96898 | -51.86225 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3200313f-f117-3687-b2de-86717d69a673 | -5.36306 | -43.20698 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| a95072b9-42c3-3dc6-9765-bf28b5cbc675 | -5.42186 | -45.86943 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c43ed727-c2b9-32c4-8270-ed2524bb0656 | -3.93261 | -56.01854 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8a04253f-478b-3d7d-bdda-7de9699f0331 | -5.09275 | -46.22469 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8be898a2-3c70-304b-9805-8c832418683e | -2.08745 | -46.57087 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| bdff57d6-a28b-38a7-9732-0764b7268a5d | -3.31169 | -53.70646 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1e7f08bb-8052-315f-adc8-57d4497ccb14 | -2.30911 | -57.98231 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 729ad7ce-3e1c-3d0b-9d2d-3c4e8141b970 | -3.50995 | -43.83026 | 2026-10-08 16:39:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fdeaf960-276c-3506-98c3-fa713257c863 | -4.01001 | -59.06187 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77135b88-a8de-376e-a269-dc0b4e8da3b2 | -2.90611 | -54.02315 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fea7a2c5-9e15-3d06-b6bb-772364e93a07 | -2.76238 | -54.10317 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 3696709b-5dd3-3d3b-a56e-9fb0f493ac45 | -3.08682 | -58.03235 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 132a03a6-a95f-330f-92fb-7126c05f9b19 | -5.09899 | -46.19905 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| eda83510-4e37-3575-86ea-1ee6cd5894ea | -2.09565 | -46.5802 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d19be3f6-0a89-3760-92e6-97d394f62c95 | -2.74744 | -54.10014 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 32332ede-06e0-3e80-8bb3-aad83c25dc79 | -6.22543 | -52.77892 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f5f75177-3154-3ec5-8cce-491d6f2f527a | -3.46835 | -39.50694 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 78bd2b78-13a6-3e91-b2cf-c7947509538a | -2.64301 | -55.71641 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b4a840d-51bb-3f3a-b093-61664655057d | -4.21633 | -44.80121 | 2026-10-08 16:39:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cbd4743d-42f7-37e1-a193-fdbe1e547d59 | -4.20339 | -41.7596 | 2026-10-08 16:39:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 79c2fc61-2c75-30a4-9a5c-10f1e5826751 | -4.15531 | -55.16237 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ff4bbcb-11a8-305a-b738-5cd45fe3a9d7 | -6.72578 | -55.05839 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 67efffc7-c8c7-3549-9c0c-7bf4673c59c6 | -2.15787 | -59.22643 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| dd36c15f-cdc2-35fe-80bd-325513a85bba | -3.25633 | -57.19039 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1d07b5e2-a528-395d-bf34-ec63ff0aa6d7 | -4.77454 | -42.68064 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| dcfff1a2-0c8d-3c75-b119-b9be5d6ffcb4 | -6.20554 | -46.64824 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c0005f31-740d-3bec-9cd8-1ec8053010db | -4.69397 | -42.90114 | 2026-10-08 16:39:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5df21692-a665-3fc9-8302-71bb252f6209 | -7.23501 | -55.13359 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 0fcbf748-341f-3709-bede-4519f04f13c8 | -3.77506 | -58.52534 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c0265dfc-129e-3194-9061-041ae2d9d1bf | -3.01168 | -54.74824 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24a63071-8ec3-3387-b66b-8b3b84122c8d | -3.86394 | -44.12918 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e5feb9d9-72e2-300e-8f46-0e4ec171e157 | -3.18308 | -58.84021 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9bfcbd39-4f79-37cd-b70d-ce79ce8b0552 | -3.20956 | -53.86029 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bfc5fe6c-d456-38da-9afd-7c1510944c9e | -4.36239 | -55.22476 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 768e2fca-dbf8-3593-9b54-4f8bcdb355fe | -3.01915 | -54.76397 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f3939187-c033-30c5-8c1d-b9d16c09fb4b | -2.50915 | -47.37764 | 2026-10-08 16:39:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| aef22088-2ee8-36e6-8e1f-5e7a29503d1e | -2.93519 | -56.59004 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a5a31cdc-9673-319c-a3ca-af07a96aef3d | -5.50177 | -42.84956 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f309319c-4cc5-3a1f-8a97-d2bdfec49ed3 | -3.37074 | -43.02797 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f88414e-97eb-374d-93c5-3bb1231236ce | -5.70089 | -53.49292 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 46712e2e-8a7d-373f-ac71-5f5197031c05 | -2.07593 | -56.87682 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b5b4a99d-9b34-330d-a4e0-d36ee912cf07 | -3.69255 | -43.05241 | 2026-10-08 16:39:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README350.md)
