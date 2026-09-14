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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5121774f-9dd8-3199-b0f4-eb1c2ab6dd57 | -12.29618 | -42.30283 | 2026-09-14 15:46:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 7343153c-1ae1-3048-97de-3ec720d734bd | -15.50735 | -39.66548 | 2026-09-14 15:46:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 85e01603-198d-380e-8438-290d5d4b7d1c | -11.51919 | -45.75824 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 24a03758-64cc-34ba-aa1f-2e4923969e0b | -10.81412 | -46.30489 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 773bd7a5-369d-3f81-b57e-22f3938ca29b | -11.19332 | -45.40477 | 2026-09-14 15:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 66bdf4ea-8a2d-37de-a1d4-635dc380e453 | -13.67349 | -42.34219 | 2026-09-14 15:46:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| acb8b92c-b2df-3d89-9d15-215bf2d9429c | -15.26465 | -42.79031 | 2026-09-14 15:46:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cbf9600b-6ece-32d9-9d4a-125915455759 | -11.36307 | -43.96874 | 2026-09-14 15:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ad6f3a5e-de26-3060-93c6-50b2be68000f | -14.23212 | -41.14549 | 2026-09-14 15:46:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 7e924819-d7f5-395b-aaa1-581e7f7ba151 | -12.48228 | -41.41389 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a40abe97-ac49-358c-a4a7-8dcf24c85331 | -14.45387 | -41.99797 | 2026-09-14 15:46:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21fdd0a7-85be-3d3b-ab90-66ce31085ef0 | -10.30744 | -45.33917 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 8aa371f1-1083-3ef7-af80-98b2647c83b2 | -11.51435 | -45.75945 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2e3b7798-5ef5-32ae-8b88-fff734bf4023 | -15.46234 | -40.33994 | 2026-09-14 15:46:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f1ef2d41-b915-38c2-90aa-23cc1e1a45af | -10.30961 | -45.33611 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9802833b-5153-3a44-ad0e-968f1a8e0105 | -13.96997 | -42.45558 | 2026-09-14 15:46:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e0e0d80c-db6f-3daf-aa8c-afb315be4a7b | -10.77823 | -46.30992 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f4408a9d-853e-3042-b398-4f52075b7e55 | -11.37511 | -43.96227 | 2026-09-14 15:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| e69c95cc-1f23-31e0-a222-5bdac056a06e | -10.79726 | -46.25755 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| a2a3e60a-3fe5-322f-b7d0-3bdea8607cff | -10.78505 | -46.24186 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| deb0821d-de9c-3b93-b30f-1268c3dc028a | -10.82335 | -46.29652 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cd080279-f874-398a-a490-f335cdc23115 | -11.17438 | -42.79348 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6eaf4044-d887-327b-ad51-9cb153b90abb | -11.18376 | -42.82235 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 28e9d004-2924-35be-8c96-8192e14cdd38 | -17.26441 | -43.97499 | 2026-09-14 15:46:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26073968-45e2-301f-a337-a70b6bb350b5 | -10.42225 | -39.31045 | 2026-09-14 15:46:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 098d58a4-94bb-3709-b41c-e4407568e00b | -12.48814 | -41.41676 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b73ec12a-a0d5-3b45-9502-22c162a2d51b | -11.18071 | -40.52308 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 38.4 |
| dea7d529-bdce-3bbb-a637-f22c2e1751e8 | -14.89643 | -41.18646 | 2026-09-14 15:46:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 47962495-5c2f-37ca-8005-995011f4d73a | -14.05698 | -40.21331 | 2026-09-14 15:46:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66205b2b-8fb6-39a4-86b4-2a47ee6dc0bf | -10.7694 | -46.2963 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6193938d-42a6-3c06-857c-856e8c9e85c7 | -10.80355 | -40.84626 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1a26d578-5649-34c6-955e-565b0efae14b | -17.59811 | -44.34086 | 2026-09-14 15:46:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 16a0ff13-8c2c-32b8-ada8-209cf6be8063 | -14.40859 | -43.65906 | 2026-09-14 15:46:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82714902-6f09-3882-b5e0-bf4eb5d46811 | -14.33388 | -40.15476 | 2026-09-14 15:46:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 5cd4a5ab-95a5-3f80-a4ed-9463c7b46b42 | -16.18911 | -41.88427 | 2026-09-14 15:46:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 34b0bbb3-5f06-3eff-af74-6f33306bf87b | -11.11421 | -40.48015 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| a38c2fdb-b368-3f39-8c7f-6332cfd7ecfe | -13.56853 | -40.63842 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 389d6eda-017a-3a23-bab7-755a3e48d43a | -14.82819 | -41.12785 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| deec109d-1692-3539-b12e-19bce77102e9 | -10.82026 | -46.29488 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dbc226b0-58ce-3e8d-a31b-0e09114dc355 | -10.79396 | -46.25619 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| afd3cb1b-e4d9-3f7f-a8d2-cf4627286548 | -10.78927 | -46.25087 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| ce14a961-60f1-3e8b-9a1a-15d4fe099043 | -12.25428 | -42.09322 | 2026-09-14 15:46:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 396e8187-dafe-339c-8315-e16da49f2215 | -14.37084 | -41.38231 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7817bf5-237d-3347-ac57-6033f1305c11 | -14.51965 | -41.12072 | 2026-09-14 15:46:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 09e3305a-6bcf-38a3-b598-c836015680f2 | -11.52622 | -45.75739 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 477.9 |
| 0a18cde2-d722-300b-acfc-b3c3ee569f3b | -13.67302 | -42.33798 | 2026-09-14 15:46:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| bdb18c4e-8e9d-3c08-81c9-fc091ed35e64 | -11.21313 | -43.43694 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6a41f507-d619-3daa-81c6-faaf8545b19e | -10.65372 | -39.47437 | 2026-09-14 15:46:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 87eec566-d30b-3174-8716-f75e2b11c44e | -11.6826 | -41.30785 | 2026-09-14 15:46:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| dc09a59f-abab-3116-b5e9-f0180be7f2ae | -15.16505 | -43.84333 | 2026-09-14 15:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e85695e3-0904-3c28-9410-c277acc46844 | -13.57329 | -40.63357 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| c3031691-0ffb-3e77-85d6-38074feac9b6 | -16.00249 | -40.68056 | 2026-09-14 15:46:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 4fa1844a-212a-38ed-98ea-ef93ced95a9e | -14.16517 | -42.20599 | 2026-09-14 15:46:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a807fb26-a91b-31b5-857a-ec8d8458a5db | -11.51994 | -45.76509 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f3efcb52-bb64-3c06-a9f9-85c3ce2d9f04 | -14.56361 | -40.86472 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| fcfb9ec8-c3a0-3599-b498-d24c8fbefa23 | -11.18073 | -42.79696 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6d3369b8-7905-3ffa-8dcd-c2fc6e69a676 | -10.53192 | -46.30649 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d071315c-0360-303b-8899-b7d49a0f509e | -11.19858 | -39.69183 | 2026-09-14 15:46:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 75cee65b-1907-3f0c-8e01-5f1784354d66 | -12.22496 | -39.29616 | 2026-09-14 15:46:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 9505956c-2a03-33a1-8d08-e5f8e4e93106 | -12.46743 | -38.3511 | 2026-09-14 15:46:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| b5127777-62b4-359b-9bae-d2325d3f0103 | -15.17219 | -43.84829 | 2026-09-14 15:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c7fc0fd0-7138-3d9a-8498-c4bf1a531933 | -14.752 | -41.09789 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5f194522-9efe-3d7f-ba9f-81c539cc2892 | -11.1033 | -40.47445 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 28713598-e4bd-38ef-83d7-5b5255ee67ed | -10.83463 | -46.29309 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| bf9ffa8b-0dbd-34c7-b1c2-28f07d5ab6b2 | -15.26481 | -42.79143 | 2026-09-14 15:46:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 052198e3-abf6-3e14-ab61-810ca5376c36 | -10.81137 | -46.25356 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 579cd89f-277b-3f87-a308-ea461769bc54 | -11.51514 | -45.76624 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| d9e6598f-2fb4-39f9-9f41-401460c18e78 | -14.34828 | -41.43132 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 50.0 |
| 424e5332-87b3-31f2-9b70-0b775117eae7 | -11.18861 | -42.81313 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 138746c4-3ee7-318b-8b7f-812f81449920 | -14.30124 | -40.81136 | 2026-09-14 15:46:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 78756617-9d85-391f-99fc-f4c2082d214d | -9.73669 | -37.166 | 2026-09-14 15:46:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 74339580-43d8-3c57-81b5-6d1bb5bd6f3b | -11.1881 | -42.8089 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 32acdd0f-0c38-3afb-b6c1-2a10a82b5ac0 | -12.06977 | -41.71499 | 2026-09-14 15:46:00 | NOAA-20 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 556509cf-a742-3854-b973-ff652b85cc5e | -11.24471 | -43.44257 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 32d59711-d71e-3427-9875-e3ff1ec80ca7 | -14.37759 | -45.25457 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ffc83fd0-9b62-3485-9c1f-4405fd96f0c1 | -10.53679 | -46.28519 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 13ba5fcd-0398-320a-bb1a-7d23821f70d7 | -12.4819 | -41.41061 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2acf27e8-d43e-33b1-9675-249b9a1b16ec | -11.29331 | -41.60536 | 2026-09-14 15:46:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d35ec057-f909-3b8b-b114-37a2cdb1d478 | -15.03007 | -41.38887 | 2026-09-14 15:46:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0365cd9e-5766-30de-b297-1acd91e6d8e0 | -14.65162 | -42.02818 | 2026-09-14 15:46:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 714c7465-86ba-3826-aef9-8386baee4168 | -10.30681 | -45.31186 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 00659d96-28d0-3f59-87d8-03ee0c207e5b | -10.83772 | -46.29462 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e6192896-b605-3848-bf82-201bc254431b | -12.33202 | -37.97443 | 2026-09-14 15:46:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0d0b8aa7-bc6f-3e9a-8f46-c73eb7e8f17b | -10.54318 | -46.27746 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| f276c26b-a0b9-3ecd-90c7-a312988ffb96 | -10.81536 | -46.29015 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 40489c26-3ac8-325b-ab06-61c960322089 | -12.48307 | -41.42055 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| be4ac87e-5b00-3b0a-a6ba-41797b637552 | -14.57379 | -40.76317 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 33470d4c-45ee-3920-bed7-1bfea6864da3 | -11.23861 | -43.44331 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 25dc5c9a-2fe8-3581-b099-02e6af24b885 | -12.17739 | -43.54779 | 2026-09-14 15:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 894b6fe1-651d-3278-911e-8c94a9d76558 | -14.38576 | -41.5814 | 2026-09-14 15:46:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b6c9688a-0d3a-3389-944a-2d5b734af43c | -11.62863 | -39.78231 | 2026-09-14 15:46:00 | NOAA-20 | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| de2b473f-05f9-3360-8a46-fb68be4821e4 | -11.29917 | -41.60823 | 2026-09-14 15:46:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 85048a3f-c7f9-3a93-b54f-e535dc2eedd3 | -13.29187 | -41.0076 | 2026-09-14 15:46:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 757cc29c-6360-3033-81b6-f30dc0718fb1 | -11.52845 | -45.77782 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 6c45302a-4036-309d-ac27-cbff508cd348 | -14.4931 | -40.84348 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6340b5ec-8369-3d7d-a337-31730b54f88a | -10.79551 | -46.24141 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 80268f21-e9ab-39b8-b2a0-f4ca98fd69f1 | -16.53127 | -39.81579 | 2026-09-14 15:46:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2b694b1d-2175-389d-bbb5-ad3653728447 | -14.61225 | -40.76691 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 65d4020c-7481-3480-b6fa-cd0e74f17ad4 | -11.51356 | -45.75259 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6eaa0d2e-bad6-32e5-b6e2-3ecf417954a6 | -15.26509 | -42.7947 | 2026-09-14 15:46:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README85.md)
