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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e77730c8-f8e4-368c-9266-5cac83a041fb | -10.72254 | -48.24825 | 2025-08-21 00:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8485ba9c-e2da-3108-8966-a0cf3aecb0be | -13.15463 | -46.90298 | 2025-08-21 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| af6a3c12-4e04-3380-b7b0-af34fec2cc32 | -11.49678 | -50.53671 | 2025-08-21 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 65531010-b97e-3f36-8c58-0dc666fd63b5 | -14.85491 | -47.93071 | 2025-08-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5f576523-da0b-3bc3-9f53-bea0d1d92fed | -8.7941 | -45.42914 | 2025-08-21 00:28:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7513df9a-ee12-3c88-9bc0-61452cbe48dc | -13.04504 | -45.18294 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8c11ba64-8ebc-3461-97d5-13242c84c83b | -9.92016 | -49.28499 | 2025-08-21 00:28:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ad25c0ea-2285-3a56-8ad6-427473dbef92 | -13.39064 | -47.49446 | 2025-08-21 00:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| a605699f-d745-33b8-9c88-270ab2ca02fe | -12.98516 | -45.21684 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| ebd9f7b9-9385-324e-a121-17a1d24e6a52 | -13.65457 | -45.72234 | 2025-08-21 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e64f03f7-68d0-3b9d-ab01-246eb86e3ea2 | -13.13326 | -54.92316 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| fb712535-1c75-39aa-aa8b-bb0deb866d35 | -11.81418 | -44.26694 | 2025-08-21 00:28:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5c1b6f81-c030-3693-b460-ce1d350dd2a9 | -11.91243 | -44.87286 | 2025-08-21 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0282f382-55e0-34c0-86a0-cc98eafd5e0d | -8.83607 | -52.05093 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 687edff9-5c96-314b-bc40-5f397f017b2d | -12.98384 | -45.20761 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 010b3890-6a3f-345b-b6ae-118c3e62c146 | -13.03873 | -45.20869 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| f564ca77-236c-3b6b-b20e-73e17ae7b012 | -9.31629 | -48.93343 | 2025-08-21 00:28:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c0778f2-9c11-32f0-8757-424859b8266e | -13.03743 | -45.19945 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 22e972fa-bcae-3541-935f-094f35c91f83 | -13.6533 | -45.71328 | 2025-08-21 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| d320ce4e-7c80-33f6-be7e-5ece375a98bd | -11.32169 | -55.2154 | 2025-08-21 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 09ab8b05-9034-358e-a8ca-48584ff97867 | -12.63786 | -46.88667 | 2025-08-21 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 09f35b88-1189-39d0-87f5-419ffc4c8fea | -14.85762 | -47.95149 | 2025-08-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| d197ff2e-10cd-3536-8234-fbc240abc595 | -12.64429 | -46.8673 | 2025-08-21 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b50e78a6-ea73-3515-aca4-62d1783c56c7 | -14.85627 | -47.94116 | 2025-08-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 6674b55c-9bf7-30ab-a132-d665c6504085 | -12.8951 | -46.07788 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 76f5e337-7e57-3574-8310-a9f836fec803 | -13.03612 | -45.19021 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 1c0627e3-7c13-3e6f-a973-1eb3c1e6ca96 | -13.02457 | -45.17311 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 3d2cca69-3d29-38d2-a61c-650476ea5b65 | -8.77221 | -45.47137 | 2025-08-21 00:28:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5e6505a5-1eb3-36ce-ae6b-5f9dde259366 | -12.21783 | -45.39726 | 2025-08-21 00:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| da4cee76-a5b5-3fe9-99f1-76131d67059a | -14.84826 | -47.95293 | 2025-08-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f840f1fd-3674-34c1-ae6d-c0409fd47502 | -11.91381 | -44.88241 | 2025-08-21 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 45606ce3-69c2-3b4f-b1d6-cdcd16163f05 | -13.04387 | -46.83165 | 2025-08-21 00:28:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 183bac3f-2515-3242-bede-947bbff22107 | -12.63663 | -46.87765 | 2025-08-21 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 18784b55-7ef5-3d41-89f8-3532e19ada50 | -12.95169 | -46.22586 | 2025-08-21 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7c5dac39-ee70-324f-a2da-782e6ece5379 | -11.49513 | -50.52354 | 2025-08-21 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c402070c-ef44-32c9-a2f5-2db0ed3b2586 | -8.83814 | -52.06736 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 4b1947eb-a87b-3a89-9dba-b7851d5c75f8 | -12.9441 | -46.23616 | 2025-08-21 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 24a8f269-a36a-38f4-920d-66d153cabdc5 | -11.81268 | -44.25683 | 2025-08-21 00:28:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 4498afe9-5222-3a1b-bdb7-8dc89d4dbed0 | -12.98253 | -45.19838 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0164382d-b1bc-3c2f-ac0a-977adeb98c2c | -14.49678 | -45.94869 | 2025-08-21 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 097ecf9d-009a-3ea9-b3c4-b9a8de242db3 | -11.09188 | -44.80711 | 2025-08-21 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 490e7f6d-7f25-3675-84f7-1ef929399a93 | -12.22676 | -45.39598 | 2025-08-21 00:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| b65553f4-c6d5-32b1-ba8b-e73174795648 | -10.97809 | -55.24777 | 2025-08-21 00:28:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| f528f07b-ee29-38d4-b0ae-2a03e2b435a6 | -13.03089 | -45.15324 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe1fbbda-e686-3e57-a61c-7d84bb92f034 | -13.01432 | -45.16522 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 1a0310d2-0a98-3a4a-a89c-1d9e6a1df82d | -12.22806 | -45.40518 | 2025-08-21 00:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| b6ae2466-68b1-3e0d-a5a5-4b9bd9e1e633 | -12.67177 | -44.95992 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2869ee61-29a6-3686-9a21-ca03dbdd9c35 | -14.47182 | -48.36789 | 2025-08-21 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e3440de2-2332-39ff-8f32-e0944a8a8daa | -13.0298 | -45.21005 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 83903842-bb1b-3052-931d-e097ba9a5975 | -11.43678 | -47.33089 | 2025-08-21 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9d9727b9-b51d-32ac-a552-4e32a75e431f | -13.38289 | -47.50573 | 2025-08-21 00:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 47f97aa4-c98d-3277-8eeb-a52fb63e36a2 | -13.27654 | -43.91953 | 2025-08-21 00:28:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6955c7f-1b66-3867-82bd-ab496f236879 | -13.0322 | -45.16249 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 16a89c87-5874-339b-a5e9-ec2e90897677 | -14.88184 | -48.06394 | 2025-08-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a01cbaa-4e1c-35dc-89da-3963f0f030e1 | -13.6544 | -42.48355 | 2025-08-21 00:28:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| c9c7a341-a4a6-35d8-9f38-e6d12a3318a2 | -11.02345 | -44.5969 | 2025-08-21 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2f50dff9-5a41-3912-8354-5a5f23f1aff6 | -13.04137 | -46.81334 | 2025-08-21 00:28:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3a5c3e1e-7090-344c-a382-066b67825b01 | -12.71985 | -44.78221 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| decceb7d-3007-3416-aa77-b4334b39a9cb | -14.4892 | -45.95909 | 2025-08-21 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d558d277-a706-3eb8-bce0-658e0e77625e | -13.64446 | -45.7146 | 2025-08-21 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8d232d77-deab-3aea-99ed-4b36c6da5d7c | -12.95419 | -46.2439 | 2025-08-21 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 465.7 |
| 8f1a6f0e-007e-34b4-aa4a-09afc721d380 | -9.91653 | -49.29127 | 2025-08-21 00:28:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 57eb61ec-38ed-3a9e-a92e-b0e7c0db4485 | -13.3314 | -40.34401 | 2025-08-21 00:28:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 164681b4-b6cd-31b2-9dd2-daff843523ba | -14.84553 | -47.93196 | 2025-08-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d1e1594c-1a37-3b89-8c06-fe8b7e34ed6d | -9.30243 | -48.42744 | 2025-08-21 00:28:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69e75ed2-bad3-304b-8236-8fca4935cd31 | -11.29569 | -44.94148 | 2025-08-21 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a683e924-0bed-3275-af69-2c87151137c4 | -10.53825 | -42.54877 | 2025-08-21 00:28:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| d6a59403-e534-3deb-988b-e04229e33124 | -10.45735 | -48.80921 | 2025-08-21 00:28:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 66599ce6-7509-3d4d-9e77-b893376da1ba | -14.67296 | -47.24736 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7bd0d813-4d8f-3a11-bdee-707600557953 | -14.50687 | -45.95645 | 2025-08-21 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fac28e8e-77d4-3e80-863e-0845b41f934e | -13.54129 | -47.03984 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 937bedaf-3720-32b5-8737-8bfc4e0ccef4 | -13.53233 | -47.04114 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9756a8bb-20e5-323f-9065-39d30295f6b3 | -12.08498 | -44.72718 | 2025-08-21 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ca4b8ca3-0596-30cf-82f6-87982423652a | -11.43554 | -47.32176 | 2025-08-21 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 35daab0e-a381-3dee-8883-b4208ded8e81 | -13.02326 | -45.16386 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.5 |
| ceadfd8d-2aee-3f9c-8132-f74e2ca9316f | -13.39189 | -47.50385 | 2025-08-21 00:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e7e4cd9e-68ea-3114-93fb-5e7128c8882d | -13.14821 | -54.94749 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 88ca7ce0-00ed-35f5-86fc-8c6e28a4bfb0 | -12.08471 | -47.90739 | 2025-08-21 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fc4ed1c1-2379-3f09-9132-b076452d05d5 | -9.85746 | -44.69125 | 2025-08-21 00:28:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 646a2f38-4587-327e-b417-0aeb08f8158a | -10.72123 | -48.23839 | 2025-08-21 00:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d5580ab1-5399-3bad-98e3-d2ad1c16d0b6 | -13.14866 | -54.92144 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 0863e7b9-a51c-3783-a664-22b953023c84 | -8.06865 | -43.67975 | 2025-08-21 00:28:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d2c30422-e662-3077-a7b3-8623db1dd8f2 | -12.08599 | -47.91701 | 2025-08-21 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 67beef0a-797a-310f-be27-9bb2d524c630 | -13.03351 | -45.17174 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f4290ef7-f558-3284-802f-2d26bab6e007 | -11.09328 | -44.81681 | 2025-08-21 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 125cc733-5e3f-30f7-a20e-75e909063a16 | -8.79547 | -45.43874 | 2025-08-21 00:28:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f80e5ea8-9b88-3ae7-a7dd-e19189ef57c8 | -13.01826 | -45.19294 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20ffefc8-f01e-3b72-8a70-61b1b6853581 | -12.96053 | -46.22456 | 2025-08-21 00:28:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 96a0dd50-fc20-3997-bc56-072ded9abb71 | -13.04372 | -45.17371 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c48875e2-f9ce-3286-86f4-f7727d8a7284 | -13.01957 | -45.20218 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 41dc95e5-8491-3563-bce1-a00a4ae49981 | -13.04262 | -46.82248 | 2025-08-21 00:28:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 32471ea6-c72c-3096-a82b-4d9337c0baae | -9.55355 | -48.10655 | 2025-08-21 00:28:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 668794ac-23d1-3111-bf85-683524ed92dd | -9.03288 | -46.59509 | 2025-08-21 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ffea16d2-83de-3a5a-ac0c-484036cbfe44 | -12.95294 | -46.23487 | 2025-08-21 00:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 452.9 |
| f1e747b0-6e0c-3171-8b5d-7be268fbf62d | -11.4343 | -47.31263 | 2025-08-21 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4488e482-8995-3908-896f-728365eea6d7 | -13.14503 | -54.9166 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 72f2b4ea-0f2f-3104-be1e-954378941f3a | -13.65644 | -42.48962 | 2025-08-21 00:28:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| fb18b425-c237-3f1e-9f5b-67f1bfe64684 | -12.97359 | -45.19973 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 519c35e9-116a-3723-95c6-2491ef59ebda | -13.59367 | -47.01639 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4d3bae88-e91a-3f84-aa3a-301db0da0124 | -13.38597 | -46.23287 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README3.md)
