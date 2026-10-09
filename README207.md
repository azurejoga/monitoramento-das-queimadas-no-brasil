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

## Dados Diários - Página 207

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f531b1f0-04a9-3a69-820b-f2847da0cee6 | -3.43414 | -54.54983 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 803b6225-2258-3534-8645-df142fa88baa | -3.53477 | -59.51105 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96e115ed-007c-3f6e-ae8c-0a03381c67ff | -3.38769 | -59.43028 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63d1e61c-25a6-3011-af5b-c3b56a3674c0 | -2.99006 | -54.0708 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5bf83bb-4ad8-3ec6-8f0c-a851c39f5bcb | -3.71387 | -59.64424 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b48529c-2903-352d-88d3-574bfc1c605e | -2.91891 | -58.53278 | 2026-10-09 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f907ab9e-91ff-31d9-a49d-34b1845df798 | -3.00408 | -54.09465 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 266d12ad-6c90-3b50-b4ef-43a99e46248b | -1.98643 | -56.844 | 2026-10-09 05:23:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82a700f1-d526-30da-9b88-2718173ee54d | -3.63416 | -59.57032 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dad14013-7197-3058-b8be-cb0e4eabbbbd | -3.22844 | -54.30154 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db54b7fa-7983-3c45-bf4f-dfcc08fb51a3 | -0.2509 | -55.91327 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a5562c0-da57-3c31-ad21-25b262648d0f | -11.25688 | -46.27826 | 2026-10-09 05:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9263b77-f79a-31d7-87be-9c5fbd9191e7 | -2.56606 | -56.16868 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03641144-674d-3ce8-8287-06724ae162b6 | -2.5846 | -56.14077 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3b06739-fdc0-30fb-9773-e0d3c7fb8d7a | -3.2113 | -57.86609 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e67a6cae-ec43-3b38-b5a0-fddbc9847dbe | -3.18637 | -50.58208 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e3694fa-333d-391b-8c1d-2c9513aac3d1 | -3.17906 | -54.74786 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 968b87bd-7c0e-3ae1-803a-60364109b2f3 | -3.08707 | -53.96479 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 882bb290-d3c7-3efa-a26c-79085c319e48 | -2.08484 | -46.57642 | 2026-10-09 05:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42a8d740-43ee-35aa-9c26-e837ef2b9152 | -8.75429 | -62.62173 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 39fcc26b-7f3c-3b4f-8b38-d6a3bba74149 | -3.05585 | -53.93524 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 886f390a-8b0e-3033-a82e-e0c441fefc31 | -4.51583 | -54.89606 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 050f868b-c432-36ae-a109-9bcaa15847e0 | -9.29339 | -47.4653 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f5885a4-cc0a-3ed0-a088-ecb182997b52 | -3.45275 | -56.9081 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1711977d-f28c-39b3-821a-43c4463fe39e | -3.18951 | -53.95204 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c14f4dca-18ef-39de-b14e-ce464036d2b7 | -3.2109 | -50.55249 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d21d364a-df7a-3bf6-8f8f-37fa0db01679 | -3.28499 | -54.00897 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d329558-0827-38c5-8eb8-49a470981ff8 | -3.97413 | -59.33317 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35289c49-e0c0-3923-9865-b00c7ac3d3b2 | -2.5099 | -56.14459 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d873f866-cc1b-3d29-bd59-9f157e13edfb | -3.17906 | -54.74787 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fcf3740-d242-31e5-b277-7bf4ed72686e | -3.0803 | -58.09263 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec7acff4-72ad-3404-8858-51d723902ef8 | 0.50218 | -50.77713 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ade69d9-8518-3ea8-9419-53f437274c87 | -3.77306 | -60.72001 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 601e10c1-95e1-38ba-893d-b6ee920ca17e | -3.56998 | -54.67042 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3ef04a8-cb71-3626-be70-6aacee305103 | -2.49718 | -56.18099 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10464c43-e636-3350-abba-19bc4db68e80 | -2.47641 | -56.09381 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27d73186-6caa-3f76-a1c3-4b47b79f2812 | -3.0079 | -54.10758 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b421cc41-c75e-36a7-8049-ed60738fd275 | -3.07748 | -54.27919 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 976fd404-08b8-3c13-a849-0bfeb77d2eb1 | -3.84225 | -55.83696 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c45abe3c-8131-3729-aeb7-f89f9483fe14 | -2.49889 | -58.07516 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bca8878c-4248-3c2d-b96e-ef50256f0f6a | -3.15714 | -59.08651 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37b9cf13-9ad2-3e02-bda9-6994dcf00030 | -1.18344 | -54.18382 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5fb38b76-735d-30ad-a4c7-43a4ec8b1ef0 | -3.53479 | -59.48944 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dafa06d9-1d55-3ccf-a978-fce775c86910 | -2.3599 | -48.88713 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 723e8411-4a45-31a1-8a14-094bc1109591 | -3.1796 | -58.83832 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e0fd76d-01e2-36f0-bf06-6e8f73f8ed31 | -3.53251 | -57.53173 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 403386c0-61f8-3952-a789-05439f189c5f | -2.22413 | -60.07875 | 2026-10-09 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3628ee28-f773-3df0-b3a6-c0ef2dc8c15f | -2.50733 | -56.25114 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5347f9dd-f7e6-36ad-b42c-a316cee8d787 | -3.20607 | -58.00678 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 489e289b-2fc9-3757-9eb8-28c0a08e6af9 | -11.40384 | -46.68013 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8948a3cc-b648-3374-9085-f98280d3def7 | -4.80399 | -54.67685 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99b561e6-13a8-346e-9955-00785b1f4a26 | -3.59512 | -61.64349 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35843563-fac0-389a-a855-93f5e583cba5 | -3.43083 | -60.22882 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22ef575a-abc0-396c-af4c-a525f7f92b35 | -8.99638 | -45.91064 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1cd0703-5c12-33b5-afc0-b97e05027840 | -3.27993 | -60.99474 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09f7c13a-8967-399c-b04e-b094506e97e3 | -3.11795 | -54.16232 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| dd54dcb9-c59d-31b5-9fce-a9d907270c3a | -11.39839 | -46.67866 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 414bfcf6-52a3-385c-99c8-306f09e0f017 | -4.62359 | -49.21069 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a513fef-adfa-3bc9-9673-ec5810cf2646 | -1.32445 | -55.43684 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b297f5e-903b-38de-b028-207b0c991234 | -3.57174 | -54.69097 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 09b6581f-b941-3b3d-a20d-4fee11e38f7e | -4.35403 | -55.22886 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d918d3d-7058-336a-b669-24ea218336e1 | -3.16429 | -58.63463 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 782f8883-10d5-309b-ac03-14d6124d16d8 | -3.52865 | -59.50648 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5369055d-dae7-3627-992f-bb2202ee2b66 | -3.32686 | -61.26564 | 2026-10-09 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9efc010-0b03-3a86-8a7a-77383d28bddb | -3.34998 | -50.48 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11407402-da8d-367e-8ca3-dfe131805274 | -3.6466 | -59.17128 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 360e8d2c-951c-3236-a5e3-0c25947b05c6 | -11.31733 | -46.65808 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a860b0a-29cc-3411-bc9f-aa3ba30e6ec6 | -2.56428 | -56.1799 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ecf13eb-7e68-3377-a63a-f0aabcaac411 | 1.77528 | -55.5347 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5073b5e-b27d-3fa5-b5b0-4f657b62808a | -3.73759 | -57.12826 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f232ba2-52f6-37db-92d7-79ebe184f60d | -3.11428 | -54.16968 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e54f9a75-2a91-3eed-b6a2-bd257f3301f9 | -4.42744 | -55.16357 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddc566c8-5684-3430-9054-589e5b59cd99 | -9.29274 | -47.47067 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 12992a89-d75f-3241-a5be-96c014b202ff | -2.4858 | -56.14083 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| babc066c-8e9a-30e3-9a31-a07064e58277 | -2.02781 | -56.94507 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af23a514-b2d5-3005-bb18-1870a882c1b7 | -8.33866 | -49.13011 | 2026-10-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75eda461-6106-3f02-a382-6c77ef9e2f7c | -7.75578 | -54.95528 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c5b0a4c-f2d2-302f-a22e-a5f92b828662 | -3.39893 | -60.84238 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17d4cb13-54d7-3868-a94c-5acaf89dcd35 | -1.20263 | -55.70247 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3003416a-16f6-3b69-bd15-6555def65d2c | -2.3949 | -57.89341 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ca815b0-ff85-3785-aad7-7ce430fdce51 | -3.52823 | -59.33769 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6960b1da-5c00-39c5-bcd9-e9cfeec69d67 | -8.97429 | -45.91373 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c24456a-9ea6-3382-b28c-23e92ba44eea | -3.02399 | -58.94123 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8762488c-e754-3f79-b2d5-fd46b477c9a3 | -2.02964 | -55.62794 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7314f01f-628c-3638-af82-dce6ef6cce13 | -2.73439 | -57.4641 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8f1d3b3-7723-3692-8cdf-7ac4a77f0f23 | -9.24862 | -62.31028 | 2026-10-09 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43889299-ebf5-3f00-9189-fe23596dd3f6 | -3.19215 | -50.54409 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de9f2be-de3d-3861-b576-9ab802b9a00a | -3.06047 | -53.93097 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eba1ca48-08fa-34ea-acb0-19595024a4b9 | -3.58399 | -54.66056 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16766a48-bfdc-3ffe-a32b-fc2624ec23e2 | -3.5663 | -54.6763 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71edbd33-f324-3189-881b-2302ff2935ab | -8.70273 | -61.40352 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c27b25a6-1d38-359b-ab2c-5f38b77a4330 | -3.77001 | -58.84357 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b7f893af-ccfb-34b4-8352-67b2287bbc2d | -3.30973 | -54.70319 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcce88f9-0762-3179-904a-e06ce761c6fc | -4.51514 | -54.90068 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e75fa87-9846-3b25-9a78-3738f36cc40d | -2.83746 | -54.1272 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 610e8f1c-bf91-32f4-a5a1-bb9584e47b9d | -7.2247 | -55.0843 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 40bf35d2-6f5f-36af-ae81-822afe17861a | -3.59254 | -54.57863 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e86a4daf-1613-382f-8bde-8e5647b095e2 | 0.94433 | -50.20211 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fd10119-836c-3140-926c-01961f54317b | -3.71559 | -60.16162 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b824e623-f106-3c34-a69a-6069531fc50f | -3.54188 | -54.62927 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README208.md)
