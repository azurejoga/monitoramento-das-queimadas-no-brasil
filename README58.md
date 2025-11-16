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
| 1d18c528-03ea-3917-b764-ca90d22fc220 | -12.69317 | -46.7915 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b5bb82f-d772-3448-befe-c3047b2b21ef | -10.11992 | -43.91346 | 2025-11-16 04:57:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a92bfb41-9a5d-37f3-bebe-71cfda08fd63 | -10.16495 | -44.5036 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe13be89-080f-31e6-a68f-274d27d9d7a3 | -10.31382 | -48.13989 | 2025-11-16 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c23f229d-a014-334b-af5a-d4fde36eecaf | -7.36945 | -43.32126 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b20c0cf5-3e2b-3cb5-a110-9b65d90ff094 | -7.01748 | -45.16098 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8387531-bec0-3301-bacf-a7806ed26fd5 | -7.04796 | -42.24703 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4870dec5-bead-3caf-af20-0719855758e4 | -12.00429 | -49.28319 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be565abe-5db0-381d-9dfc-cf690045a6e9 | -9.72294 | -48.90364 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8154dd2c-d865-3dea-bc8b-c716cb4df842 | -12.69715 | -46.7844 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ff27565-f3c9-3665-bb2d-bfe84065b61a | -11.16236 | -47.44898 | 2025-11-16 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 573345a4-7a15-3621-b67f-73355aa59038 | -5.12516 | -55.96276 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdff33b2-518e-33cf-addc-e7a7c5007e1e | -12.06429 | -48.19939 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 138b193d-9c8b-3b10-b02e-ab3fb4d92fc6 | -11.71544 | -48.86146 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f489258-9f78-3c22-b4d2-7d28b0353d19 | -11.91097 | -46.18781 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93659f5d-97d1-3a5c-a2cc-3a5b0d1e94fc | -10.00119 | -44.772 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 149c0449-1cbb-385b-9c48-27ecfca07c68 | -7.71027 | -47.29058 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97bf0654-f371-3124-b47c-197e03afa08c | -11.71103 | -48.86087 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0c6fb67b-758d-3c9e-a34c-2240c4572c6d | -9.56767 | -54.90326 | 2025-11-16 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a7dbcde-cc0e-36c5-b560-4a0edb74a4ce | -11.41747 | -43.32975 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c70fcc3-b6a1-339a-a15f-05f93f4f8753 | -11.16133 | -49.45246 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 157ea35a-73ce-3abb-9295-9748e2d5d3a9 | -12.66269 | -47.17225 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fd30734-b130-386a-b4ec-f925a99280d9 | -12.66881 | -47.16399 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ccb86eb-ab9e-3591-934d-a3b9cbe55c85 | -11.79184 | -45.53764 | 2025-11-16 04:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a266fc3b-73b6-3058-816e-547c278c4fab | -11.05857 | -45.16169 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4659bb02-68e3-3a87-94ea-a185ce4dd535 | -9.74213 | -43.94959 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b9ede72-cb13-35e7-88f6-f5fd584c22e0 | -12.21373 | -49.61516 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8a80f69-e01c-3c57-bba5-3cd49792bd30 | -6.72959 | -42.94654 | 2025-11-16 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e7720d97-1c48-3e5b-b8d1-7d5a2f3348c9 | -6.30733 | -43.78909 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 8228bbe4-7b99-3344-bc87-e826016b1f46 | -10.17183 | -44.49575 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e9201a8-4b43-3bb4-9079-14545e5ffa39 | -9.34908 | -46.58766 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ba8db71-9759-3518-8c26-af3f77b92cbc | -10.93024 | -48.69392 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 44a6c7cd-8108-3cb6-a091-a8590bce04ad | -7.26653 | -48.02569 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a4fafc9-f849-395d-9a3b-5c1e705a077a | -10.53983 | -47.91808 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72f2d59c-b770-3698-9554-e18991c3e97b | -8.20672 | -43.57121 | 2025-11-16 04:57:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3abc60c5-db49-38f9-8abc-6af743b09d9e | -9.06098 | -44.75376 | 2025-11-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9af8af91-3f51-3587-b96d-9fa5b99f8527 | -6.71681 | -42.94904 | 2025-11-16 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a7e714d-bea0-3e23-8d2d-9e80af5aa4ab | -11.20186 | -49.41248 | 2025-11-16 04:57:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a681332a-c659-3be2-8616-f6742876e238 | -12.06168 | -48.21903 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 472eba4d-e19b-3ab8-a829-f54f6fa686eb | -9.72473 | -43.9646 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c1dad2b1-23ea-370b-94b4-b78722f82aa0 | -12.19295 | -47.44578 | 2025-11-16 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70783352-ba8f-3a34-8fdd-5eee50cbfade | -6.44756 | -47.27699 | 2025-11-16 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a76b3083-457d-3c88-ae10-4c4008fb1bad | -8.32221 | -45.40966 | 2025-11-16 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ba5a11-8b2b-3e73-a88e-b8b2158ee88f | -12.20557 | -49.54909 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b47ceca-b030-35be-adce-78f7fba3741e | -12.06631 | -48.21972 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61dab764-3897-3d29-ba49-5569862fc496 | -9.51039 | -47.27554 | 2025-11-16 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 182a58b3-c221-3ff2-aa5f-3b4a238a4bae | -7.72025 | -47.28674 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3b4d4ec-b709-36ec-8a3c-9077d0477d85 | -12.40566 | -47.56015 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9708f97-b962-39a8-af92-5be21059e188 | -12.69428 | -46.78221 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f8dcb14-70e8-385d-a247-21d714219766 | -7.15054 | -41.76008 | 2025-11-16 04:57:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ffba4b44-2994-30e6-b48b-68afffe74e17 | -12.66807 | -47.17003 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5b0693f-0da0-37b0-88de-5b4dcb12ca83 | -11.16608 | -49.44915 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7fca363-18b2-3eb3-8dfc-1f95f1d83865 | -7.21959 | -47.97946 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9494bb5-d391-3ea5-92fd-2b0a80fb8624 | -6.17894 | -48.06202 | 2025-11-16 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 470d6828-84f9-3f52-b4ed-7f0d009b28f8 | -6.31256 | -43.79366 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e7cc4ebd-4f4c-327f-a770-10e9841669b4 | -6.2597 | -47.08241 | 2025-11-16 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c455617a-d388-39c5-a6bd-a3321c595b6a | -4.36 | -55.51884 | 2025-11-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceb79b7e-5096-3b78-8830-93de1ec2d6bf | -10.84821 | -44.09045 | 2025-11-16 04:57:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| fd0689b9-893c-341f-9205-2a7b7c1372c6 | -12.87787 | -46.45148 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b75a0a16-ca8a-3989-bf92-082c49066209 | -10.6553 | -49.70891 | 2025-11-16 04:57:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f15dff9f-dad9-36f7-8fd7-6d1e049362a8 | -6.70221 | -55.23127 | 2025-11-16 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aae24b46-7157-36dd-8a1f-866b99f963b0 | -12.00971 | -49.27554 | 2025-11-16 04:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 6dd46111-4999-3dd0-b4b6-9cbd963f0cee | -11.36153 | -49.79522 | 2025-11-16 04:57:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3db3ff24-058f-333a-bb81-ffceec168484 | -11.97195 | -44.9622 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| dbeae201-cc11-3d2f-90e5-c85fa970239e | -12.20896 | -49.6186 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 633f4896-059c-3920-a697-e8229b3dcfca | -7.01702 | -45.16429 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1ec6527-220c-3afc-9c41-91580ebcc499 | -9.33566 | -46.57414 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d65b51a5-543a-397f-ba3a-c5e8436436a5 | -9.7307 | -43.96529 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98e0f806-9f12-365c-96b5-815661c09066 | -12.86452 | -46.7792 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 213ba66f-9f46-3c46-bfc3-8965450fc7ec | -10.53915 | -47.92324 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3efeffa1-5a1b-36a1-90fc-1a12457aa61b | -7.2146 | -47.9831 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2d602da-a7aa-3c00-a777-13be17d0fc68 | -9.74263 | -43.96679 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 39871be9-c475-33ad-9f3d-218c09b3a895 | -12.41189 | -47.54991 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be11a4dc-c6c1-301f-a14a-9d7c0f79cd27 | -11.91803 | -46.21861 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ce34d26c-b77e-3146-924a-673bd85025b5 | -7.35513 | -43.33749 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa99bdde-6272-300e-aa7e-22996e9a5ee6 | -12.69869 | -46.78911 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 392a795f-d005-3152-8ff6-61fbd874e5ca | -6.6834 | -42.05031 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ec5e1d51-69a6-3c15-90f0-750a518c726d | -7.39225 | -48.6477 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1838ac55-1951-3c83-bacb-2a18dad2e9ed | -9.74054 | -43.96266 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b3116fb-9275-3dbb-8001-557d2fbd4dfd | -9.73615 | -43.94887 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0ede39bb-354f-3aa5-acaf-a8e8ff0fa47e | -10.17092 | -49.31139 | 2025-11-16 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 287ea2fa-dd27-39d7-8cbd-02348325cf9a | -10.86836 | -44.88673 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c86490b3-53b9-3edf-b676-f342a8bbd4c8 | -7.22834 | -47.98085 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dce16aa9-109a-3650-89f5-4768ddd3a9c3 | -11.16646 | -47.45513 | 2025-11-16 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4ca7e9d-eb14-36e4-91d9-b39e43ba08df | -10.00589 | -44.78053 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11d1c953-46b4-3c70-92da-93b1b20c1141 | -6.67693 | -42.04425 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d934ccab-8c02-3579-80ab-f16df91ff457 | -11.70929 | -48.87403 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6234fd87-76c4-360f-a1b8-02317d1fe62b | -12.21883 | -49.54692 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc85d09a-9c63-3664-a2ba-3e04c9d4b4a9 | -8.31773 | -45.40264 | 2025-11-16 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32b92e9e-c7a0-3b3b-bc72-48f9d7c8678d | -12.20052 | -49.61744 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| df0b03e3-9133-3808-82d4-f5cdbdb9ad47 | -7.01124 | -45.16689 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df736697-9d9a-3319-b754-524d567e9a55 | -5.73917 | -51.04392 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5765d5c-2ada-38c1-8497-d8cfff1a7c30 | -9.74376 | -43.95795 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f6ebe35-9561-304f-a05f-08b80aceb7bb | -11.91341 | -46.21951 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 542582d6-478d-37a2-8b46-645375d81c00 | -9.68431 | -56.09846 | 2025-11-16 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be6cced8-4a90-32d9-980f-cc4002dad65b | -6.67765 | -42.04391 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dfcffc6d-959e-3c8c-9050-f015cafd3ecf | -12.69082 | -46.79295 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df993697-0508-3633-9d01-ef92116c06b8 | -7.0165 | -45.16126 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10c993f9-a9c3-3043-b1ec-96bc14a06e1b | -5.08204 | -50.62593 | 2025-11-16 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f5afadd-0d63-3126-b88d-65387b73b988 | -8.96055 | -47.52207 | 2025-11-16 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README59.md)
