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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe9a36c4-bb7c-3e14-aa20-abcab1f45674 | -13.37412 | -40.54904 | 2024-10-25 15:31:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 23b1484c-8325-3678-a5d5-d06a752ba1ef | -13.3736 | -40.54459 | 2024-10-25 15:31:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 33.8 |
| b7de2dba-ef85-3e14-a96d-9bac6815c7cb | -13.37197 | -40.54546 | 2024-10-25 15:31:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 6e985dfd-cc7d-3e19-952f-ec6dc41bc8a5 | -12.95575 | -40.64978 | 2024-10-25 15:31:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 33965811-b638-3a74-8997-9cad42619bdc | -12.95154 | -40.64915 | 2024-10-25 15:31:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ace65331-22cb-38f4-a1af-e65a6820daa9 | -12.951 | -40.64464 | 2024-10-25 15:31:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4b32e54c-0ea1-3bd1-afc7-77a7d43cd2e8 | -12.94976 | -40.64972 | 2024-10-25 15:31:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| cd81b340-c55c-3517-90d4-26204984a198 | -12.94499 | -40.64442 | 2024-10-25 15:31:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5a587129-93a2-3e41-b67e-85cad4f76360 | -12.79362 | -41.82702 | 2024-10-25 15:31:00 | NPP-375 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4186961b-7b74-3897-bc9e-c9b0c905c426 | -12.60964 | -40.73947 | 2024-10-25 15:31:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7cf8acba-6778-3480-b738-8cdf5c12183d | -12.50001 | -40.86444 | 2024-10-25 15:31:00 | NPP-375 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8e33e297-dc07-3a1d-b3e8-9008890ace6d | -14.73956 | -41.17425 | 2024-10-25 15:31:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 5e9032ff-46bb-3768-9311-cf5ad73fb3a4 | -14.57555 | -41.87185 | 2024-10-25 15:31:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 7fa73a56-71e3-330e-8429-c45edbe8ae68 | -14.57495 | -41.86629 | 2024-10-25 15:31:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 0d128329-105e-3600-8e8e-2da6d81ce6a4 | -14.56605 | -40.76398 | 2024-10-25 15:31:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9085add5-d3e4-3cc5-8bee-6039a1717d85 | -14.5049 | -42.08181 | 2024-10-25 15:31:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b7c09805-200b-388a-ad05-5b8883504d60 | -14.50434 | -42.0763 | 2024-10-25 15:31:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c2b8d0dd-d7ee-3cc8-9597-59992bdb7475 | -14.49189 | -41.05604 | 2024-10-25 15:31:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 350fdf00-c524-3410-94af-29b85c1d9380 | -14.4536 | -40.69231 | 2024-10-25 15:31:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 117145e5-b949-35a6-a3f8-29875ecf7335 | -14.42036 | -42.14515 | 2024-10-25 15:31:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| ff1819f6-0490-3d7c-8cd5-b803f841f5df | -14.41978 | -42.13956 | 2024-10-25 15:31:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 32fb0136-6bd7-39ec-80e3-2920c00a4e60 | -14.41875 | -41.06753 | 2024-10-25 15:31:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 18663d5d-7c9a-383a-9568-70bbcc22e1fb | -14.4182 | -41.06242 | 2024-10-25 15:31:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d8fb2b79-2d57-35b9-b9fe-1a11289e46ec | -14.39082 | -41.40601 | 2024-10-25 15:31:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d234c5f7-356e-3099-b6c5-2f869744843e | -14.3881 | -41.4045 | 2024-10-25 15:31:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ad3df5bd-35cb-3050-bd41-e659b18f6cd2 | -14.30487 | -40.701 | 2024-10-25 15:31:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ded7f587-7789-36a7-b30b-794285d5bd07 | -14.16331 | -41.35867 | 2024-10-25 15:31:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8e46c187-d527-33c3-958b-c5cfb6192ffe | -14.16035 | -41.35965 | 2024-10-25 15:31:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a32310a7-f149-32b5-96ed-06fbefdefc3c | -13.96326 | -41.42189 | 2024-10-25 15:31:00 | NPP-375 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d0d82822-c3b7-3e09-9978-9e99384c5056 | -13.73934 | -41.58858 | 2024-10-25 15:31:00 | NPP-375 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e10d0c2f-60d2-31d9-99f8-158e50d831ac | -14.70359 | -40.89146 | 2024-10-25 15:31:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| dadb00b3-c9a2-363d-87d5-35e0e61376a2 | -16.15758 | -41.72781 | 2024-10-25 15:31:00 | NPP-375 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 43f151fb-03d9-3b43-88a6-7e990975b05e | -17.05809 | -41.90806 | 2024-10-25 15:31:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| d6125d2e-87fe-3daf-8d53-70cfd58ff22a | -17.055 | -41.90971 | 2024-10-25 15:31:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 00684687-250e-3216-af7c-b1d4bb6247cd | -17.05444 | -41.90334 | 2024-10-25 15:31:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| fa0aa0e6-3ee0-3df3-95e4-b686977e6ef6 | -17.0514 | -41.9087 | 2024-10-25 15:31:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| dfc644d8-ef1b-3714-988a-7a771d30d868 | -16.9983 | -41.8451 | 2024-10-25 15:31:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| fda079b0-1714-3738-93b5-92ed323238a9 | -12.20856 | -42.35942 | 2024-10-25 15:31:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 59ca6d27-de74-326a-8bfd-3b27c234333e | -12.20205 | -42.36017 | 2024-10-25 15:31:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9bb1e39a-91ae-3a87-907f-c2120ccd9590 | -12.12498 | -42.1929 | 2024-10-25 15:31:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d01bd417-27d3-35d4-9820-0c52229deac9 | -12.0984 | -42.24763 | 2024-10-25 15:31:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| dfef2304-73a6-324b-af5f-7bfe36bbe22d | -13.76706 | -42.33531 | 2024-10-25 15:31:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 33.2 |
| bd8eaa0e-5200-37e9-a797-122b76880c67 | -13.7665 | -42.33012 | 2024-10-25 15:31:00 | NPP-375 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 7d1118df-545f-38a6-9663-32608f085a82 | -13.76482 | -42.33356 | 2024-10-25 15:31:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 12d5abb0-d61a-347a-9f8b-55e29fbea144 | -13.76431 | -42.32848 | 2024-10-25 15:31:00 | NPP-375 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 9226d4e5-c4d5-30c4-883e-4a0c69c96459 | -13.59159 | -42.55493 | 2024-10-25 15:31:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 49967956-f5ac-3096-9acf-be7dfcf38448 | -13.5558 | -42.60355 | 2024-10-25 15:31:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 90b8ed08-25a3-37fc-b3e2-1dc235261a1e | -13.46684 | -42.58553 | 2024-10-25 15:31:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 54a60a86-dec0-37c5-b302-8d7ada71403e | -13.46296 | -42.5895 | 2024-10-25 15:31:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 9450690c-d237-31d7-964d-373b15ebbf7f | -13.46231 | -42.58306 | 2024-10-25 15:31:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2bf6a916-992c-3eeb-adfe-bf52b4f04a84 | -13.42166 | -42.3535 | 2024-10-25 15:31:00 | NPP-375 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| bd772d48-5ac7-3a78-83e9-c05f911e02a4 | -13.52086 | -43.42943 | 2024-10-25 15:31:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d12e0f7f-df6a-3207-b323-3450f0b02d0b | -13.51161 | -43.47858 | 2024-10-25 15:31:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8fdd4ab-94f9-33ab-a51a-07b59866e592 | -12.96746 | -42.5907 | 2024-10-25 15:31:00 | NPP-375 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f2d8fd1a-3931-3a75-b8c6-c4b2fa4c5e6d | -12.87608 | -43.05645 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 84fe4862-28c0-31f2-98e6-4c7fcbff2b8a | -12.87607 | -43.05452 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 3139ca99-7d55-30e0-8ede-dc9493f21f2c | -12.87546 | -43.04854 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 7c04be77-5969-3a2d-9d94-711a41511479 | -12.87543 | -43.05047 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 21612fe0-b92c-392f-8775-1487a9bc008f | -12.87484 | -43.04239 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 49.3 |
| 36f3437c-7618-3f37-bfbb-7b39b56bfa49 | -12.87477 | -43.04441 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 0e38c801-0691-3a8f-aee9-09fcd5dfa627 | -12.81799 | -43.23294 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 44cc6680-5edb-3336-abd9-81274a864788 | -12.81733 | -41.92595 | 2024-10-25 15:31:00 | NPP-375 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 14a1cec8-435f-32b7-a5c1-cc5eef709e5f | -12.81729 | -43.22651 | 2024-10-25 15:31:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 6c519d72-615b-3b34-85f6-f7f68bc115ce | -12.78386 | -42.73906 | 2024-10-25 15:31:00 | NPP-375 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7b08fe88-4ff7-3cf4-926a-2f654cf1d150 | -12.64188 | -42.87562 | 2024-10-25 15:31:00 | NPP-375 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b18e9a6b-c5fc-3bdf-bb53-5b88850195bf | -12.64124 | -42.86946 | 2024-10-25 15:31:00 | NPP-375 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 3eea9781-c2eb-3005-9ef8-4a77a621dc92 | -12.49671 | -42.41818 | 2024-10-25 15:31:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 12398fd0-ea27-392f-b569-13898b87c3ee | -12.22866 | -42.9258 | 2024-10-25 15:31:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d213e1ca-9834-30b1-bc53-3fab72e36884 | -12.22703 | -42.92777 | 2024-10-25 15:31:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1e55d3d8-86cb-34eb-bbd5-8adc841326c9 | -14.76557 | -43.03335 | 2024-10-25 15:31:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 19.1 |
| d53e6a6d-289f-3919-9e56-aafadcfb95ad | -14.76495 | -43.02669 | 2024-10-25 15:31:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 32.6 |
| bbcb73f0-cc7c-32ee-a089-ebe677641e44 | -14.70487 | -42.75668 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 048cd77b-ae31-3aa0-9ad0-4fe11b89d069 | -14.70427 | -42.7506 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 65cca41f-d833-3bbf-a8d2-02956fddd845 | -14.70184 | -42.29435 | 2024-10-25 15:31:00 | NPP-375 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1ec32e43-ff9a-3d30-a290-9dcc34cddecb | -14.66114 | -42.73445 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1dae1755-1fd0-3696-84d1-ba1976f79301 | -14.66017 | -42.73631 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 85ec9135-b313-3018-a5d7-574fb5adb91c | -14.60169 | -42.26615 | 2024-10-25 15:31:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d8595264-7aef-32b7-bc40-ea0df904a32f | -14.59777 | -42.26868 | 2024-10-25 15:31:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ec8c40ec-cf83-3450-adc4-ccec1ba18312 | -14.84227 | -42.66346 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 231ad467-0dac-3ebf-ba7d-d152083c41d6 | -14.84149 | -42.66832 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| be014657-0d87-3ec9-990e-a62be0137e39 | -14.84084 | -42.66193 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 37a25ec6-9169-33e5-8451-6313057fe443 | -14.83535 | -42.66328 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| ceb54707-2bdb-307b-847c-b75109e525c9 | -14.83393 | -42.66194 | 2024-10-25 15:31:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b3b7ac58-1414-3d04-a69f-2b55273afc2c | -14.53326 | -43.06027 | 2024-10-25 15:31:00 | NPP-375 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9b7dce1c-a537-39eb-9996-6fa6c19c9aae | -14.11609 | -42.85702 | 2024-10-25 15:31:00 | NPP-375 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 249db891-8240-33f5-9ab1-e458581ac4a1 | -13.90258 | -43.22105 | 2024-10-25 15:31:00 | NPP-375 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d41e42d1-38d9-3596-9e7f-709a90999d0d | -13.82254 | -43.61126 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 42ffa20c-18e2-32a5-8cf2-7fffb7e914eb | -13.82 | -43.61311 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8101df45-9a5f-3ec7-aa93-9d9dbb590e18 | -13.73219 | -43.60019 | 2024-10-25 15:31:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 059af91f-deef-3722-ba14-8ebddaefca21 | -8.48066 | -35.18831 | 2024-10-25 15:33:00 | NPP-375 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| efbd411e-7585-3b16-a9ea-b604dcd46a5d | -9.36321 | -43.37585 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 30.9 |
| d3a78ec6-d319-38ec-b424-339a227d34b2 | -9.36249 | -43.37002 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 34.7 |
| e62ac315-d1ce-3ed8-8a37-79a88d860257 | -9.3595 | -43.37934 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 8f9e30d1-737b-3910-89d6-e7cbbd53b7b0 | -9.35882 | -43.3735 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 8b09d872-9109-3620-94fa-94e8b9677751 | -9.35814 | -43.36769 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 30.3 |
| aba95d76-b9ba-3664-b8e2-7e3e2080916d | -9.35651 | -43.37653 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 0d1079ef-16f2-3941-bc68-93d3e8b89bb5 | -9.35579 | -43.37071 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| e012520e-f6e6-3a13-869e-3b4d2f6cddc2 | -9.35508 | -43.36496 | 2024-10-25 15:33:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 1da5cc22-d655-350d-a4c8-c960730b35b8 | -9.31505 | -43.25902 | 2024-10-25 15:33:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| d8bb7b57-ca77-39ad-9116-35ec4ebc8c68 | -9.27347 | -43.47898 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |


[Clique aqui para ver as próximas entradas](README121.md)
