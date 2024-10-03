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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4de00c4a-d5b5-31af-bdd0-be4ab21dc4a6 | -10.69239 | -58.53949 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cbf3b98-bbcc-305b-ac9d-6ab13fc04ce5 | -9.46743 | -58.97212 | 2024-10-03 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13c8dbf9-7808-3c55-8603-9526fcb4c1d8 | -9.4664 | -58.97743 | 2024-10-03 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 92a73ff4-0232-332a-a2ae-3588978fc416 | -10.9523 | -58.96432 | 2024-10-03 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60d3c607-a590-3a36-b554-e0e53a5e9587 | -7.19828 | -59.79488 | 2024-10-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a427e31-49b3-308c-832a-8748faa85b3e | -9.90717 | -60.086 | 2024-10-03 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd8a6b47-afb9-3b7a-9126-c8e0f0a53f72 | -9.90594 | -60.09221 | 2024-10-03 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7fa6a44e-0d33-3c19-a6fd-63db98a09ec5 | -9.39217 | -61.05253 | 2024-10-03 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| bc8c99f9-8e56-323b-83cb-3f6058223aac | -9.38505 | -61.05113 | 2024-10-03 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1d067c62-9962-3037-9c8a-9563cff42adb | -10.37947 | -61.21048 | 2024-10-03 04:27:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0fac517-6bf0-3341-9e51-06bd2ffbf7cd | -10.37801 | -61.21746 | 2024-10-03 04:27:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5b9ce8e-5d8f-3b60-860a-fb5f4e479688 | -12.3089 | -60.76029 | 2024-10-03 04:27:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6a67fe4-1fc0-3b20-8736-d6e7e32088d4 | -12.30221 | -60.75903 | 2024-10-03 04:27:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7377dddb-da5f-3eaf-8ebd-7c947690a837 | -9.35737 | -43.25546 | 2024-10-03 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0e711d9-821d-3ebd-a370-cbf43c49832d | -9.26576 | -43.50258 | 2024-10-03 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ed55d5b5-9162-3c3c-ab83-181ca0b1bb18 | -9.25609 | -43.49236 | 2024-10-03 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1616ce1-3538-3338-ab97-46fac3ffa3ea | -9.25546 | -43.49664 | 2024-10-03 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| be2842e4-1792-37cf-86c6-63ebd801d491 | -9.25182 | -43.49607 | 2024-10-03 04:27:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 735b48e9-098a-307a-9af4-9e423aa01f09 | -8.31463 | -42.82818 | 2024-10-03 04:27:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39fa201e-0219-3a16-8759-5684db0306c8 | -8.31156 | -42.8231 | 2024-10-03 04:27:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fff8d865-8209-3975-b816-abc673a5910b | -8.31089 | -42.82764 | 2024-10-03 04:27:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dcfa9f72-f150-332f-a6bc-73017722bfa6 | -8.31022 | -42.83217 | 2024-10-03 04:27:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 73d52cdb-098c-38a1-b43d-68b5ce13fa21 | -8.18427 | -43.69883 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28da8b94-ac38-3489-9e6f-f6aec32e94f1 | -8.18364 | -43.70295 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fac8b3a4-8f66-358a-8c1a-2e3757a62cce | -8.1807 | -43.69831 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ca91d6c-976f-3718-9680-ff9073a1bcca | -8.16522 | -43.70429 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6e9f1c07-7da9-3c72-9e45-56d89b269cfe | -8.164 | -43.71246 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 49ec385e-74e6-3f5a-b910-a6dab3ff2707 | -8.16217 | -43.72465 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4964f80c-5bc8-32b2-8202-5f6277530e74 | -8.16044 | -43.71191 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0717ec51-45c8-37cd-b5bc-7f9a533f7bee | -8.15983 | -43.71598 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6223fc85-0e9b-3ca4-a4e7-f2f9aeb2aa0d | -8.15922 | -43.72004 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1303bc3e-236d-32ad-9d27-3a2206f3b4bc | -8.15861 | -43.72411 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 98fee339-6cab-3f2c-80e5-34a4a0358364 | -8.158 | -43.72816 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e158b288-d314-30dd-b749-066487576b6f | -8.08539 | -42.88505 | 2024-10-03 04:27:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0581b49e-3840-3364-b1bc-e2d43419edf0 | -8.08233 | -42.88007 | 2024-10-03 04:27:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3d508163-c0c8-3f52-9f26-6d3dd9aee114 | -8.08166 | -42.88463 | 2024-10-03 04:27:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f73207c6-9f3e-3708-869b-c5af76f1e1b1 | -8.18859 | -43.67013 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4392a37-bb68-3a5c-bccb-eb721633b216 | -8.18564 | -43.66547 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bce8f62-4207-3822-bdc8-0a4d2d06919b | -8.18193 | -43.69014 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8e7311a-3222-3f11-815a-f82ff4924b95 | -8.18131 | -43.69421 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16610340-c78c-32f7-b32b-15d694dbf006 | -8.16419 | -43.66248 | 2024-10-03 04:27:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29b8bbdf-ad87-3cad-a000-1130374091c6 | -9.50461 | -43.16995 | 2024-10-03 04:27:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8fdc5fe-2b24-3a5d-b459-880aa0826ea8 | -9.50088 | -43.1694 | 2024-10-03 04:27:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 88b1f55a-df3e-3991-8f55-355ac8908893 | -9.47292 | -44.05827 | 2024-10-03 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3f75c74-ebc1-335c-bcda-9d150fa91efe | -11.49144 | -43.23343 | 2024-10-03 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34b459ff-e65f-345b-a4ee-0bdcd7c30cce | -11.84282 | -43.82983 | 2024-10-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1abf4e4e-e309-3229-a37a-7099d6e1cb4d | -11.83977 | -43.82482 | 2024-10-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a753d711-22d0-3e79-8ef2-5c8cb401e250 | -11.83912 | -43.82927 | 2024-10-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1455b561-2b94-3b16-9d4c-0584e2bbef2e | -11.28284 | -43.39662 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7a4503b-d2e0-3d5a-860f-9c2c3dda4bcd | -11.28184 | -43.39831 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 68ab8955-d80f-3108-92bd-0c2224beec56 | -11.16397 | -43.46288 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0459430-d7d3-3ca9-aef6-2a993e7c4a3c | -13.31042 | -43.71144 | 2024-10-03 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a008a34-5e07-331e-8e26-6c0a244592c3 | -13.30663 | -43.71088 | 2024-10-03 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb655e1a-d454-3107-8b71-b66a1b06722a | -13.30629 | -43.71305 | 2024-10-03 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c979a39-7f00-335e-9b66-299d552cdce5 | -12.99615 | -44.72262 | 2024-10-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e437538c-52d4-37a2-a8cf-afa546da5654 | -12.99317 | -44.71791 | 2024-10-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d53c9df-b110-3d90-aef6-692a317db198 | -12.99257 | -44.72208 | 2024-10-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffc0ea5a-4a30-3964-99be-c37077b5fc68 | -14.84136 | -45.18299 | 2024-10-03 04:27:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5ee3447-c324-3f7b-832e-082f013d94a7 | -14.5155 | -45.2388 | 2024-10-03 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aac85e56-ffcd-35b7-9987-6176f82bc97c | -14.51254 | -45.23414 | 2024-10-03 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3fd083d6-e6cd-35e9-afa7-ed30e4017ad7 | -14.51016 | -45.2254 | 2024-10-03 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5309e0-cb12-3eca-ba9a-e52a151c7fdd | -14.50958 | -45.22948 | 2024-10-03 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12179c23-cad4-3a80-b916-0aa37e6e97b3 | -14.509 | -45.23359 | 2024-10-03 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fc282e2-bdb7-39d8-9bbe-7a6c1aa07e05 | -14.10213 | -44.20549 | 2024-10-03 04:27:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afa169eb-1aec-356b-ba56-a9e910ccf9c6 | -14.10075 | -44.20263 | 2024-10-03 04:27:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb467f8e-68bc-303c-9131-b0e3e9315be8 | -14.04642 | -45.05952 | 2024-10-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b7196d8-ffb8-308d-8c4c-3462506a1cfd | -14.04286 | -45.05901 | 2024-10-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 664af193-6553-3a12-b23b-f09a1ecff6a6 | -14.0393 | -45.05849 | 2024-10-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e27a0c05-6a73-3d30-afb7-98ad36e49381 | -13.99198 | -44.03179 | 2024-10-03 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4088c80-ce78-3e72-b30d-c5cb1086a566 | -15.45689 | -44.30909 | 2024-10-03 04:27:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c0051a7-abb8-3c47-8d13-e8108c4b0ec8 | -7.87535 | -44.96736 | 2024-10-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fc56ee3-73df-3e19-8f2a-1056efedb274 | -14.1961 | -46.46016 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 262f54bf-af56-3ece-9655-be4749e5f248 | -9.00464 | -45.20217 | 2024-10-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9906fffc-8845-3ff5-b0a6-4305461fd4bf | -8.96363 | -45.24461 | 2024-10-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45715355-8a57-399b-b6d6-3ffb9f71f0a0 | -8.9597 | -45.24772 | 2024-10-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c70e3556-7c13-3d19-bd5f-3f9d8b7ae4de | -8.93515 | -45.63479 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75683dce-3eed-31e8-8494-6feb66f01fe1 | -8.93406 | -45.64192 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85dd6fea-612f-39a2-8864-74512944a4c9 | -8.92738 | -45.64085 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57d83409-415b-3899-87bc-e25374d84d1f | -8.9123 | -45.62756 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4fb17a8-e4c0-3b10-8f8c-7111b0b6b31f | -8.90131 | -44.10506 | 2024-10-03 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c73dbe76-ee53-37cb-8920-349420b8280d | -8.85637 | -45.50578 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 09394e30-01f4-34ea-8f59-8d3a7cff9f1d | -8.85583 | -45.50936 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fa2b6bd4-75a1-31ff-9827-886fa6d7ab0c | -8.85528 | -45.51294 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa66acc1-c5f0-3298-9621-e196a5b6b06b | -8.85473 | -45.51653 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9dcdad7-d989-3797-9ec6-28d2e587a20f | -8.85247 | -45.50884 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e5155ac1-fef7-3e78-bf78-b348c827f03c | -8.85192 | -45.51242 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c417d0b0-1a02-3f04-bc55-600dc1ac0277 | -8.85138 | -45.51601 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1dd3fe9-0dfb-3d0d-9d9f-f6d92597713b | -8.84912 | -45.50832 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e071b77d-a694-30b0-9a0b-98efd7539e32 | -8.84857 | -45.5119 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a689a041-8b96-393c-8cfe-8eb2018825b8 | -8.84803 | -45.51549 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 897b3d65-61db-3a97-a76b-fd7839d971d0 | -8.76964 | -44.48177 | 2024-10-03 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4404afcd-0f29-37c5-ad80-95412254be5b | -8.32635 | -44.74867 | 2024-10-03 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a5a88317-8b9f-3db7-9d69-40dd725f26fc | -8.18829 | -44.36551 | 2024-10-03 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bca1cfa-88f5-3caa-b8fe-12025ea8ee55 | -8.18771 | -44.36933 | 2024-10-03 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dccd3327-9888-36d6-9e11-0fddb0b24d4c | -8.18713 | -44.37315 | 2024-10-03 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1a843d20-e163-3a57-95ef-7b4050997d5f | -8.16696 | -44.45932 | 2024-10-03 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c13f98a-7e2b-37ff-bea8-ac3f59a29e61 | -10.78692 | -45.54465 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e806e3a-c500-389c-ba46-5322dd7d3e15 | -10.78416 | -45.56297 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 893cf998-76f1-3bd6-bf6b-d8d7a8b5383d | -10.67032 | -44.50093 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f28242b-0211-3990-9d90-ec8c3b9ae562 | -10.66327 | -44.49986 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README88.md)
