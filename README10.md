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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e127ebcf-cb54-39b4-8719-4593adc53ffd | -6.07138 | -49.40053 | 2025-10-17 00:13:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a6b1e41e-f221-3e70-864f-21522f0ba726 | -8.20821 | -43.30623 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f24d90de-9799-3c4f-8186-fde7468a235f | -10.08365 | -45.34899 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 65ecf3f3-0260-3b25-91fd-8de76b7396b5 | -5.96203 | -42.80839 | 2025-10-17 00:13:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4b5df5f2-9d16-3b91-a637-aa18f03541a0 | -7.10809 | -44.73214 | 2025-10-17 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5888db65-9695-3058-84ea-48053bc36f2d | -10.53138 | -44.50974 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8129b535-b940-3c8e-9d99-f1c8a6ad520a | -11.75964 | -51.18578 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f13c8868-17a3-30ed-a43f-5aecf8209437 | -5.49873 | -47.31098 | 2025-10-17 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e9929f98-5de0-30b5-a693-c68b3f83d08b | -6.40771 | -43.48391 | 2025-10-17 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8658850-1834-3ba7-868b-9c1c01567b34 | -5.09333 | -45.42636 | 2025-10-17 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 7afbddac-ba35-330e-8068-e4ad95c26890 | -10.51546 | -43.38754 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4bc775c0-7ed1-3dd0-bb04-18ea2bc1b1d5 | -6.75982 | -42.38197 | 2025-10-17 00:13:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fd8a584b-2164-39fb-8730-304d301292a7 | -4.51066 | -46.01365 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 8bade201-4a99-3935-8db0-63ca07b4135c | -10.64928 | -45.24268 | 2025-10-17 00:13:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 68d8e0f6-7a5d-3d16-9a3e-1738a247c075 | -9.65135 | -48.71753 | 2025-10-17 00:13:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4ddcf64c-202f-3abe-934c-38860837a801 | -4.55283 | -43.06995 | 2025-10-17 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89462ea9-c59f-3a39-a1cc-f79bccd77b68 | -6.22208 | -47.03217 | 2025-10-17 00:13:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 990ef9fb-b474-3668-a89a-43099efc4d0f | -8.84065 | -45.96621 | 2025-10-17 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 523b147e-1cb5-31ef-a7f5-5dece80e94d7 | -5.0396 | -49.22401 | 2025-10-17 00:13:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5cd3ad32-5c8b-3dbb-8a9d-3f9febf0946d | -10.11283 | -44.61876 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8530f70e-9bd9-338f-b7ef-73e8b3469aeb | -8.30682 | -43.41539 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 8ee291e5-cade-354c-a106-8359fd19da81 | -4.37903 | -43.41369 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9573d1b-7266-3996-a268-fb0d6312205b | -7.86074 | -42.87383 | 2025-10-17 00:13:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1adbe3de-5080-3588-befc-cfa0cda30aab | -7.94962 | -44.1544 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 20b887ba-c18d-3e06-9a53-ff1f83980641 | -6.15714 | -42.81766 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| acad8f6d-9335-3fe0-a509-df37b1a9fdc2 | -10.49911 | -43.41441 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9b1920b9-5d8f-3bb3-982c-67557bece834 | -4.72335 | -46.15566 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7188ee95-818b-3fc7-ad7a-68b511d6ae5c | -8.30178 | -43.4439 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 020b9b73-979a-3ae2-b008-2a8abc58a2da | -5.65952 | -46.81197 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 41133457-2def-38cc-99ac-eae7885bc979 | -6.5891 | -44.37711 | 2025-10-17 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 06daedd7-8485-3e82-b0ff-b01a4f8b4919 | -8.30939 | -43.43354 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ad1f74f2-daaf-32af-829b-6f75c20708ec | -5.15077 | -46.05323 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 596bb7b1-ef84-3d81-83ca-ccef62fc6246 | -5.1662 | -45.22147 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c98e3be7-fa32-3da1-a3b4-995483944ce4 | -5.27026 | -43.26327 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 2035f71d-8bf7-346b-8f52-b85230dc8b48 | -8.23666 | -44.83341 | 2025-10-17 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| dacf74ae-cc29-3815-9f9e-f51a2233ba42 | -7.17934 | -42.36164 | 2025-10-17 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 592e5245-6d34-3179-885b-8f42cb602c20 | -5.39769 | -43.24831 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 741de52f-925d-379d-b3c6-3d580637f550 | -5.83643 | -45.53581 | 2025-10-17 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 599f942d-8370-31df-a712-244a109eb88c | -9.15225 | -41.06796 | 2025-10-17 00:13:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| db02130f-6542-330a-b2df-426cbfba52bb | -8.22737 | -43.31272 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 927dd81f-c85e-367b-9161-a3d5dfc9977a | -10.53411 | -49.55964 | 2025-10-17 00:13:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 9df37722-1a2f-3c6a-b8a4-9e5ce00774c0 | -8.3991 | -46.23128 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 9fc89945-a52e-3bd2-9adb-ec6bc429d940 | -4.95573 | -44.96748 | 2025-10-17 00:13:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c453c171-3657-3780-9ab9-66870f1a9aaf | -8.20973 | -43.9719 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d0c64a72-d842-349e-a9f0-0ed1e7113acc | -9.38668 | -46.95082 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9bf6fd40-8a0a-307b-8dd0-f293fe0b183c | -6.32328 | -44.32526 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ffc70bb6-beb2-3152-b28e-1fc725b53dc4 | -5.29751 | -47.93091 | 2025-10-17 00:13:00 | TERRA_M-M | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 24680d6a-2e29-3be2-a34e-80c1020c7ae7 | -5.88422 | -44.75724 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5bc1a5d8-abb7-3265-a76f-13c12d118902 | -10.71166 | -44.48106 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 799c7390-608b-34df-b022-6c584d5e62bb | -5.46383 | -44.64357 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d9bce131-6229-3312-adc2-759819cb58db | -5.87982 | -43.92165 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8c3b236d-466f-3c89-b049-71f79857c385 | -4.75817 | -45.40793 | 2025-10-17 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 0b151e9a-44df-3b33-9864-bd04a13e648a | -8.2095 | -43.31532 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 957d4425-ba4d-33be-b77b-9547e0336451 | -10.70279 | -44.48228 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 27b9eb11-3a68-36a3-b836-ab24a7d2a810 | -10.12404 | -44.55549 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8e1e850d-7bea-3566-ab8e-da4b4366a5ae | -7.47823 | -46.90617 | 2025-10-17 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 09bd8908-dda2-3090-ab94-a553e695e6b2 | -9.72999 | -44.51439 | 2025-10-17 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0d985061-60b2-352b-b99c-c15ea73501b0 | -9.83934 | -49.31257 | 2025-10-17 00:13:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1e27d099-69a3-3d1c-9c6e-f75664e08f70 | -4.37634 | -43.39454 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 462af2b8-141e-350e-ad3d-76130bab19fd | -10.18578 | -49.50504 | 2025-10-17 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 444d2a2c-06a9-3427-a43b-4e204f228a4c | -8.82108 | -47.30119 | 2025-10-17 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a75f1418-bdba-3bf5-9be7-696dbc2db796 | -4.41435 | -43.3988 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 530.3 |
| ef5b14c5-77d2-3fed-9341-0d0465c68e02 | -8.29535 | -43.39857 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 19d9e7a3-d408-3f0b-bada-c19fde66718d | -5.5082 | -47.30964 | 2025-10-17 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 19c6b1e8-736c-3598-b2d8-1d13d10c8f0f | -5.8654 | -47.58892 | 2025-10-17 00:13:00 | TERRA_M-M | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 94a58144-0e07-3c2d-a914-74aa078b22db | -5.445 | -45.17274 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49140575-7416-3bbc-b2f1-8f951ba03f57 | -6.18128 | -44.09785 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e93dbbd5-9471-336e-923d-ffd8a013d88a | -5.46141 | -41.01743 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2bedd499-aad4-3837-85b5-feaed94e8e66 | -8.30811 | -43.42447 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a74b7ec9-1912-33be-850e-78a4083ae2d4 | -8.39644 | -46.21169 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a925b079-31bd-3542-9b16-0b4066ecbb43 | -10.95605 | -49.78691 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0d09190b-8c00-3caf-88be-e931e454e4bf | -4.39468 | -43.39192 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 6364c784-94cd-3896-ab26-ecf14c25eec7 | -10.28221 | -44.03733 | 2025-10-17 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| a3039439-7505-3fd0-ba23-89ece03b386e | -8.29406 | -43.38952 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 087d14ba-a8c0-3cc7-9138-87bae2fea52a | -10.63353 | -47.43344 | 2025-10-17 00:13:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 926b89b4-eb4e-3c69-b13f-fb2edba1c697 | -5.02798 | -46.09501 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9894ac8-c6e0-36a0-bd4f-4a0bd26ea0ee | -6.74343 | -44.16208 | 2025-10-17 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0f120ec3-2b56-380b-9463-f011ac78fe39 | -9.06069 | -48.8508 | 2025-10-17 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2b961c0c-1456-3ceb-8b3f-b0a82e2f4933 | -6.37345 | -43.56991 | 2025-10-17 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ce6cc46-89d7-3216-a9a6-3b97b42c69a7 | -4.87972 | -45.55606 | 2025-10-17 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f9c44f80-57f6-35a3-a260-737acd87595c | -10.43482 | -45.01922 | 2025-10-17 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 47ea5d05-fd0f-3260-bf5d-372be872c00f | -10.30128 | -43.9801 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b22fe14-0abd-3326-9d83-fb2ddf7e30d1 | -9.34349 | -46.92326 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 170265d4-5663-34ed-99fe-d1396677d61d | -10.05722 | -43.87316 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f10bab68-b81c-38b9-b30a-eb232e1d3c37 | -4.41567 | -43.40833 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| c86f3d12-09c9-3365-8c00-fbdd3465eff7 | -10.65056 | -45.2521 | 2025-10-17 00:13:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a0dd7ebe-fd21-32fa-8df8-74d99217a795 | -4.38417 | -43.3837 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6e5c4e12-1742-38b3-8a5e-28b29d061f05 | -8.45506 | -41.26339 | 2025-10-17 00:13:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| c24206d1-f8e1-35d2-9c16-cccb808f7373 | -7.06117 | -45.06054 | 2025-10-17 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5500ffeb-2c58-3009-9777-23ac350995e9 | -11.10149 | -45.86837 | 2025-10-17 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd572778-bfda-3de2-8365-735df71d3f00 | -5.49718 | -51.16164 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b5090156-c6cb-39b0-a172-b215ea2527a4 | -7.21056 | -45.48103 | 2025-10-17 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c7a73527-dcb1-3253-a372-8a9e2fd22efd | -6.13429 | -44.2921 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 660407c5-3b29-35ea-bdbb-da14b8344f81 | -4.81219 | -45.73409 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1e558ede-9a10-3946-a3a1-e6af560ca477 | -4.96332 | -44.95744 | 2025-10-17 00:13:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f07b5a38-dcc4-3ef0-8a9a-6226d111e478 | -8.60155 | -44.9396 | 2025-10-17 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ee51cec3-49a7-3edf-a3ee-8a5188682246 | -7.75508 | -42.45319 | 2025-10-17 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 080bc79a-29f0-38e8-8cc9-a33744ecd87f | -5.35966 | -42.72979 | 2025-10-17 00:13:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 926f368e-d6b5-36ca-b209-b2b22606dca0 | -6.21703 | -44.43378 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 03af8f55-05a0-3137-a2bb-f2b6b5f52134 | -5.27161 | -43.27279 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README11.md)
