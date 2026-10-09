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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f279905-e607-3737-8820-2b7e533cc9b3 | -3.0925 | -53.9455 | 2026-10-09 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| aaba868d-779f-314f-ad94-35227408748f | -3.1284 | -54.1857 | 2026-10-09 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 61e1c24a-7302-30cd-9c8f-4981154e1212 | -13.2662 | -42.2365 | 2026-10-09 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 43b96508-cebd-366d-86fc-f7a83f9b7227 | -2.7428 | -54.1146 | 2026-10-09 03:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 044827a1-2f8a-3bff-85e8-8afa50a4b0e8 | -6.021 | -40.9577 | 2026-10-09 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 284.0 |
| 1856ecbb-2d4f-30e0-841a-6be844a6fc5e | -8.7423 | -45.1334 | 2026-10-09 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| cb7d67cb-8a92-31b8-8f9f-64529682a625 | -8.7067 | -62.4184 | 2026-10-09 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| aa129504-e0fe-379b-9dfe-72f16169f6b7 | -11.3107 | -44.8105 | 2026-10-09 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3dfa1f49-3b92-375f-83cc-a331f3945570 | -3.3455 | -50.4078 | 2026-10-09 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 063026f5-4279-347e-96c1-2f191ab1da5b | -3.5676 | -54.6946 | 2026-10-09 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4b9ce393-d342-33c8-8fb8-bb0612206352 | -11.0144 | -45.4042 | 2026-10-09 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e18d6b12-db9d-32e9-b161-84c3b65e5695 | -3.1114 | -53.7839 | 2026-10-09 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 00c5db32-1a46-3271-be72-0134a0c112ec | -13.2467 | -42.2401 | 2026-10-09 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 19c198fb-22f4-391a-b6f8-2fa15a703882 | -5.7117 | -53.4862 | 2026-10-09 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2ac6428c-1b0d-3fc5-a3ec-00fdc54b0a1b | -6.0024 | -40.935 | 2026-10-09 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| 2ad1ec7e-768b-35ef-860b-97ddaae1417c | -3.1101 | -54.1661 | 2026-10-09 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 1de3999c-5ede-3ec0-a968-12886af266e2 | -6.0019 | -40.9837 | 2026-10-09 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 331.0 |
| fd432766-767e-35a8-8da6-888b115f92e6 | -2.499 | -56.0675 | 2026-10-09 03:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 3b5c3e16-0dae-3f36-86a1-8814e4973c22 | -12.2156 | -57.1087 | 2026-10-09 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 4e102a87-7b8a-3d1b-9691-dd4ff4c3087b | -6.7365 | -55.1474 | 2026-10-09 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| c820c135-b2c1-3fc0-b138-979714edf018 | -3.1109 | -53.945 | 2026-10-09 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a16a6684-c9e5-33d8-9adf-02d28ea23e60 | -11.3295 | -44.831 | 2026-10-09 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9e918683-ea3e-3a62-b7cb-2e2eeab347fb | -12.2348 | -57.0871 | 2026-10-09 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 175.7 |
| c177acbb-59b6-385c-8a5a-f0441d49ed01 | -6.1485 | -47.2871 | 2026-10-09 03:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 9c9c8092-999f-3089-ae9e-25af4f23959a | -11.3103 | -44.8337 | 2026-10-09 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 354.8 |
| 741977da-ae48-30d4-8a80-caa714bcb56d | -11.014 | -45.4272 | 2026-10-09 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 7a91a5ab-dd8e-39e5-a127-b5f385f75cb1 | -6.0207 | -40.982 | 2026-10-09 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 185.1 |
| 49c02b46-b98b-3a60-88c2-20895cba70f8 | -12.2158 | -57.0887 | 2026-10-09 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 9cae9510-a699-3b6a-9efa-db0c37417381 | -12.2154 | -57.1287 | 2026-10-09 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1b779b9f-362a-3472-8531-3645cbfed15d | -9.8986 | -50.49 | 2026-10-09 03:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e2327f83-5da9-3447-afde-2dd7af70da8e | -5.99415 | -40.97889 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 39885655-edc8-3d0f-91d3-b286c67a9fc5 | -6.00856 | -40.96359 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| 6bb45106-2358-306e-a370-962aaeb570fc | -5.67799 | -46.36707 | 2026-10-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fbecb63-7257-35af-ad72-070b92324d2a | -2.94572 | -40.50024 | 2026-10-09 03:42:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ca07747-7b6a-3502-bc41-dd628ea3be65 | -2.07765 | -46.5766 | 2026-10-09 03:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 280fdf9b-6751-3180-9689-14565cedbbfe | -4.82048 | -45.83619 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2dfaf875-2121-3814-9bcd-36ff1d59af56 | -5.88099 | -43.41606 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5a269ab1-35c8-3e5f-a60f-f0bc9c0116b1 | -6.5745 | -35.10834 | 2026-10-09 03:42:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 98f071a9-e06f-36a2-8cff-eb34bfb8ebcf | -6.11681 | -44.81305 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc059b2d-c185-3311-958f-4d529cdd5621 | -4.8221 | -45.83553 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 776cb5e0-b34a-3234-9de4-df04583f6164 | -5.41131 | -44.62809 | 2026-10-09 03:42:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 404f79d4-a81c-3acd-b825-77323527d132 | -6.42484 | -45.94621 | 2026-10-09 03:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 76042478-3505-3c96-ba6f-fb1efe72f206 | -5.23909 | -43.98334 | 2026-10-09 03:42:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2656891-9e30-3987-831b-b6261d775d05 | -6.11783 | -44.14639 | 2026-10-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 73ee7d28-95ee-31bc-be5a-4efbaf43012a | -6.83251 | -39.39015 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 67f7cc17-2c6e-3f8f-84be-f24559ee6c8f | -5.67499 | -46.36431 | 2026-10-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33759b2b-78da-3fab-904d-e5b75ec44921 | -5.10542 | -46.2201 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e9f81c4-194c-311d-af28-f983572b00e3 | -6.0362 | -44.03478 | 2026-10-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a1a21044-4c25-3002-abf9-cf9c574c7476 | -5.87045 | -35.55641 | 2026-10-09 03:42:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06a65394-5af7-35c6-ac60-2e72ff696d5a | -6.81807 | -39.54956 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9fd9317f-6d66-3a3d-965d-707b7d4a0763 | -3.21784 | -42.96842 | 2026-10-09 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bf59f93-6d27-3301-9bf9-7dfd0919976b | -5.9549 | -40.92603 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fd57e92a-7f25-370c-b2c1-8679d4958b95 | -4.08097 | -44.12248 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 824b0a15-e104-3186-93c0-d1fb0ae01357 | -4.75776 | -44.00459 | 2026-10-09 03:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae6c2be3-edb0-313c-b7ed-1e9d07339045 | -6.84502 | -39.56897 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6e860e4-dde4-3902-b273-3c8a06b20140 | -6.84141 | -39.5648 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4045a7bc-1373-34b9-9e0a-1c70af656697 | -6.85756 | -39.46944 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af06beb7-3ed1-352f-9900-628cc97fe967 | -6.16645 | -39.45116 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 39a089b5-8ab8-3229-afac-42236907451b | -6.81873 | -39.54569 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c3dbbb7-8257-328e-9147-7a5d4cc25dfb | -5.99924 | -40.96175 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 992b2371-f39d-32bc-8d58-b2a1c541e39b | -6.01235 | -40.96954 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| d8e452e8-2e9a-3100-a23c-f6658220470c | -6.21885 | -44.14897 | 2026-10-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b71fbce-e99a-32bf-88fb-ad665c334902 | -5.47078 | -41.22734 | 2026-10-09 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 328b4790-ba66-3a56-aa8b-513a10554563 | -6.00352 | -40.98059 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 07da4fcf-9260-3176-86af-7959fd66a4dd | -6.88296 | -43.70981 | 2026-10-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c5d8926-98a2-3b0e-953e-4cc13ada5013 | -5.2386 | -43.98501 | 2026-10-09 03:42:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a437eb21-bbe5-3629-bbd7-b84cc9af5a0d | -4.26061 | -46.28897 | 2026-10-09 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4849e96c-c0fb-38bb-ab1c-947e1d7c09eb | -6.82456 | -39.56214 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 355f685f-e590-3d58-9b2d-b0a0c68afaaf | -6.82097 | -39.5579 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6f2b0f2b-c337-3888-89b6-2476bab270fc | -6.82356 | -39.54272 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd3ebbee-241c-3caf-9d8d-532a017166e8 | -6.82696 | -39.32328 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56c28846-2245-364a-9c3b-f97fca619707 | -5.98011 | -41.3812 | 2026-10-09 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 39508dd3-633e-3013-a00b-4676c651773b | -5.99573 | -40.98175 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f7665e56-6d38-3681-ae77-10d314b55e44 | -6.83304 | -39.56318 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b916d09-3d32-3f29-a6f3-5189aa046791 | -4.08688 | -44.12383 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2bfe1b73-de3d-35f5-8533-b90130a45527 | -6.894 | -39.53897 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c7373ef8-63a6-3a90-bdd2-5d8141508ce4 | -4.26738 | -46.29026 | 2026-10-09 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb88dd45-63c4-35e4-ac86-7a1a76878bf0 | -4.07502 | -44.12134 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e72b73e9-c65c-310c-800b-e825ae66e9e2 | -6.00478 | -40.95766 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| e60a878c-d5e6-3b66-96d9-669a79d3ea4a | -6.8932 | -39.53922 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5291fdbc-7dfc-37a0-a12b-f3a72ce1c792 | -6.8174 | -39.5535 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1374e2e1-5202-36af-85bc-c4372ddb06b6 | -3.21354 | -42.95971 | 2026-10-09 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9b54e9d-d4cb-3e5f-9284-ef04c53c112c | -6.18299 | -35.29654 | 2026-10-09 03:42:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e359b345-237a-3b9a-a701-2116698efe47 | -4.07653 | -44.11267 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09168070-0b43-3327-b693-d9376c9db125 | -5.98897 | -40.96524 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f80c2c7b-7fd3-38be-b109-afb36d78a1a5 | -6.10999 | -44.81629 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1eff3548-1079-34cf-b0b9-0cc3e1a5883d | -6.16889 | -35.29153 | 2026-10-09 03:42:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b3ce4161-6b17-33ac-bd0d-2f616208ab40 | -6.49226 | -43.95761 | 2026-10-09 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 182db4d4-d6d6-3ad5-b5f9-681729638726 | -6.15257 | -47.28571 | 2026-10-09 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b64f3ecb-1afe-397c-a419-bbaeaa89b7f9 | -5.09575 | -46.21613 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dead4622-e5c8-3a6d-a751-055ff28463a9 | -5.99661 | -40.97674 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7d024bb8-2297-380a-ad38-c5da4af4cf99 | -5.98728 | -40.96234 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b8a2685-ed52-369f-8751-40767a488b37 | -5.41047 | -44.63282 | 2026-10-09 03:42:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4724a9f1-3bb7-334a-bbcf-f9827847c23d | -5.33816 | -45.18295 | 2026-10-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2261d696-8ba2-3940-8815-437aa825366c | -4.98225 | -46.0461 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da201f7d-0468-3c96-b2f0-37b13da5a5fd | -5.98104 | -41.3758 | 2026-10-09 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 423aa726-37ec-3f5e-9067-53aa7512ec67 | -5.99748 | -40.97174 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5eb58c2d-966f-3056-9972-999a51f37db2 | -5.8854 | -43.41813 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f089b6c7-fa6f-33e3-80e7-a7cfd03a6f4b | -6.16475 | -44.86582 | 2026-10-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9510cef5-af7b-3d55-9ef3-9f3901387f89 | -4.81943 | -45.84195 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README59.md)
