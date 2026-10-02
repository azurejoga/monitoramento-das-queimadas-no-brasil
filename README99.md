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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a844959f-40ad-321f-b01c-221a8190f88a | -7.48475 | -42.80742 | 2026-10-02 15:54:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 001134d4-5046-3784-92fa-fdf0019ce8a8 | -11.47517 | -43.5369 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 7c94300a-cc54-37ff-8cbf-12ab347a97fa | -11.77768 | -43.55234 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 725ebfbb-61b5-3bd8-b39e-3486c2e6b614 | -11.47734 | -43.51328 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1c92499c-edc8-33fe-8c1b-1ff3ff7e8776 | -11.48873 | -43.52361 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 90a37a38-626c-3529-a87b-d71a97a7f50e | -11.71278 | -43.60414 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3b3bc512-0458-3f91-9047-dbf0ab482047 | -11.70705 | -43.59898 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c320515e-0f08-3b12-895d-e74d2dc6478e | -8.80001 | -45.82504 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 46f8289f-10b5-3ea6-96a3-58506e8c7092 | -12.31847 | -46.37581 | 2026-10-02 15:54:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e5a54d5-faf7-3384-abd8-0320346a2cff | -12.77712 | -45.14272 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f0dfd8f6-6fb0-3061-be06-874db68c4c06 | -13.34584 | -43.85226 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 9408a5e4-e6b9-3e62-b361-bad3904385cc | -11.65025 | -43.5521 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6760df60-50c9-31d8-a781-2c54335b64df | -13.34917 | -43.84369 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 67bd8fc6-ec16-3ef3-86b0-7440746846cf | -9.7858 | -44.79489 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3c530848-35d3-34d1-923f-dc0ee3dc29c8 | -12.78367 | -45.14973 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fb5d5416-f36a-34b7-b842-64d450e60605 | -11.25628 | -44.24329 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 986e6925-54f5-375f-a92b-805f744a3dd5 | -12.51534 | -44.1432 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ac206733-2e54-3811-afd2-a463a16a3ac0 | -11.72731 | -43.59775 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 989c43b2-88a8-3150-b762-97796f2c2ac3 | -11.47095 | -43.50925 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 66336db3-8120-3334-af33-4e44ce66c67c | -11.28436 | -44.25619 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6f8cbc3-99bb-36ed-90ae-31bc5d1f8bff | -11.4315 | -43.39914 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 26ccefe4-54f9-3743-81ad-824d22d96ef4 | -7.11547 | -43.14788 | 2026-10-02 15:54:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 11d11d6b-b632-3d44-8d61-3dc8d302dea0 | -11.80625 | -43.576 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9ac64c12-7783-307e-bceb-ed25641bbddb | -10.44195 | -36.54459 | 2026-10-02 15:54:00 | NOAA-21 | ILHA DAS FLORES | SERGIPE | Brasil | 2802700 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a20fb49b-9bf0-3f61-91ec-e6a7304aff66 | -12.78686 | -45.17719 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| ba435890-1162-3ba9-bfad-4e66fd22f305 | -11.72272 | -43.60191 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| f9ca7a88-8777-3db8-8c4c-49b2c427ccf4 | -13.34639 | -43.86398 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| a5273a38-d3c3-3058-a57a-3ea3af9d2283 | -12.77466 | -45.17094 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6f72123a-72f5-3620-aaa5-14cb389955df | -12.1834 | -40.5732 | 2026-10-02 15:54:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6c018f0a-36b3-36e0-ae55-51a5887ca6e2 | -11.74167 | -43.59016 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eec2ff39-8557-3633-b1ef-2258969bac0d | -11.75387 | -43.4452 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b6d2e924-f0ee-313d-aa39-628eabde3ca3 | -12.77668 | -45.13882 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 10f7ac80-7194-3351-a455-7b5e4c4d7834 | -8.13338 | -44.80486 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 77e58bc0-5c1c-3ab5-ae6e-e98467f8108d | -11.76382 | -43.44394 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| f0d856cc-11b4-3de0-b981-060f1b80be5c | -12.77566 | -41.83478 | 2026-10-02 15:54:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ab4dffdc-9ac5-3ef7-ad86-8bac7a753216 | -11.7489 | -43.44585 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 80605c77-de98-3126-9ba9-c1e4a0745979 | -11.66865 | -43.61684 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 5fe13fdd-85d5-35b1-be3d-717551ed927c | -11.42656 | -43.39975 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 62995545-ae32-3d60-bb0d-1ab6759a3cbb | -12.60795 | -41.95311 | 2026-10-02 15:54:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6b6179a8-8417-3c21-a710-88a3c9f050b2 | -11.7981 | -43.55268 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4f70e256-2220-3e3f-9d7e-51174fee6ecb | -11.70204 | -43.59976 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7dcc1e87-d1b7-3ce4-af2e-3575f227916a | -12.48777 | -44.13644 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| fa6968dc-1440-32dd-94ec-c524cf1c302d | -11.44138 | -43.39793 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e14b2987-8272-3b38-aa24-353747e840c8 | -13.11064 | -43.49348 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| de1c6966-1c93-34db-b56a-5c4bb3f55275 | -11.13953 | -44.59458 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 32658fda-d862-343f-b586-bbf418ba47bb | -12.4825 | -44.1371 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1688d081-256d-382d-92b6-a8702cf9e965 | -7.4886 | -42.80244 | 2026-10-02 15:54:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b554e1e6-3f6a-3615-af62-ada65d1a602c | -13.33985 | -43.84635 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4381c172-174d-366a-b6e1-fc7908e5aee0 | -8.96663 | -40.58663 | 2026-10-02 15:54:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9db18660-2b47-371f-be8e-1a16db2dc265 | -12.47846 | -44.14772 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| fd12a1dc-9073-38dd-bd88-3377078d923b | -7.44383 | -37.27431 | 2026-10-02 15:54:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 41d11744-0974-3b1d-b219-8db119e7eed3 | -11.76879 | -43.44331 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| de8bb158-72a3-3401-a883-500bf060fa70 | -13.33832 | -43.84167 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9d443f48-0db4-385c-8a34-0ea5eb455f2d | -11.48594 | -43.41983 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.5 |
| e6d7793d-de7e-372a-8d61-263df272074d | -8.73087 | -36.91176 | 2026-10-02 15:54:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 1f86580a-df57-31ee-adcf-3f314a59ab92 | -11.70697 | -43.51543 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b7e8a9b4-b5fc-3d9a-9269-5e4d4392e4c5 | -11.73005 | -43.57871 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| d252b72a-23d3-3fa8-ab00-d4ff57f4f333 | -12.52338 | -43.10664 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 24145c9a-be27-3077-825b-a91e2c6a231a | -11.39623 | -43.39783 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d4b85412-35c0-3647-ba6f-c986c26f50b0 | -11.79121 | -43.57845 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b156903c-af03-3385-935a-bc868feb0824 | -12.7724 | -45.15136 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fb482058-2650-3eec-aa02-be5d05be23dc | -12.22805 | -39.94201 | 2026-10-02 15:54:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| e978fd26-20ea-3147-922a-6485ae7f691b | -12.50034 | -44.15166 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 039e01a9-3d2e-3d38-b7f9-e11e2477d707 | -8.78699 | -45.81211 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f4b1803b-c70a-391b-a614-792b5e064c59 | -12.17881 | -42.06737 | 2026-10-02 15:54:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 319b08f7-f450-33f4-bb9a-e57a0a8885e0 | -11.49301 | -43.51731 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| dec6af9a-3735-31ea-9d94-0614ac126bab | -11.64597 | -43.55849 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2e3ec475-1640-35e7-8ce0-3df5d2db5506 | -11.73182 | -43.4306 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| bb7efc2c-4ee3-32e5-bfdc-f860d22d8b65 | -8.31082 | -36.13052 | 2026-10-02 15:54:00 | NOAA-21 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7f371b8f-063a-3d15-a607-dc24c7aaae97 | -11.66527 | -43.51062 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 90545e3f-6079-324b-bd73-8e1d1c345d4c | -11.7028 | -43.60443 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a15809ba-2f01-385c-a6c3-5e300a75f931 | -11.75313 | -43.43943 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8082caf2-8c37-3114-b840-dffa51696dd9 | -6.55644 | -35.5082 | 2026-10-02 15:54:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| afb304c6-0f4e-3b54-a47e-53ed9becbb2f | -9.82436 | -44.80751 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c9256e9c-6eb1-3df5-a1e4-6ea310b67c74 | -11.40116 | -43.39716 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5913af90-c464-3062-a941-b456d62d401a | -11.74286 | -43.51835 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| e677a758-b5d3-39d3-906b-dc62d4261c40 | -11.66813 | -41.58028 | 2026-10-02 15:54:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d9a7c24a-921b-3e7a-8378-fef6cb45671e | -11.78734 | -43.54821 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 91330d6f-7b34-3e1e-aeca-c75db35f8883 | -11.78269 | -43.55172 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 50e3d152-1a20-3a93-9761-0546af22741c | -9.81906 | -44.8083 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf5a3d54-f50d-3195-b9de-7b1ac51add3b | -12.54082 | -43.08631 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 50098be8-a735-3ee3-8323-0e2baf1dadf5 | -8.50934 | -36.45477 | 2026-10-02 15:54:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d0373c31-d2c8-3a5b-bb83-8b8ee9891644 | -11.81532 | -43.56676 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1183a823-28ab-3086-aab9-79818f8f544f | -13.10592 | -43.49714 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 56c6daba-bf53-392b-a6c7-bd58a6fdb06d | -11.71101 | -43.58968 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 936775f0-8292-3c59-a797-cc60b3f22ec5 | -8.80605 | -45.82768 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d881f732-bbf5-3549-a652-0912d51ac9b7 | -11.46681 | -43.40051 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f6a272cb-debd-3992-a4bd-f3574a6daa2a | -11.66724 | -43.60575 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e266ee88-ff63-3897-9bdd-13da802ef1b7 | -11.16791 | -44.60481 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3f97c052-5bba-3ebd-9878-83fd2969e7b6 | -11.47164 | -43.50806 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| db2b0805-fa65-33b1-84fa-802263ab004c | -11.70413 | -43.61687 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d1c5efff-fb72-328c-a2c1-076aee2d343d | -8.12038 | -44.80006 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 94be1c04-dcf7-3b9d-8cf8-894ec82ebf62 | -9.0548 | -46.85855 | 2026-10-02 15:54:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3fe4265a-0506-363f-a985-04b5f7858267 | -11.75241 | -43.43371 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8c71e1e5-0336-37cc-a8a9-92f62c1e5c51 | -13.35038 | -43.8534 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6ce227a4-9fab-31c9-89ef-2e4bf35305fd | -11.79272 | -43.55046 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 8d4c06da-1ac3-3b4d-be4a-bdcb3242f7e5 | -12.52351 | -43.06718 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1f81da8d-b8c6-3227-8a03-c94f0eebe178 | -10.58383 | -36.67659 | 2026-10-02 15:54:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2f482f38-b9dd-3652-9205-77d928f9aad6 | -13.35031 | -43.84513 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| f8774806-f329-30a5-98c4-8efc198c1346 | -9.84664 | -44.856 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README100.md)
