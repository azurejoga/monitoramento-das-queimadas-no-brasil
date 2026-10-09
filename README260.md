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

## Dados Diários - Página 260

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01a6c0e2-c05e-3e5b-b14a-8364167aaca1 | -12.18456 | -44.64301 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6f837a0b-bd5c-30c5-9b2d-3759d28eeaca | -16.71233 | -41.8797 | 2026-10-09 15:58:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 718a9151-ff55-3734-8b75-c70210482762 | -11.61092 | -43.60695 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 80c4e1f8-e904-3ac5-8d1e-89824f3813ea | -12.21956 | -44.83751 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d75df743-d610-39eb-aa5b-e6842641b2ec | -11.04557 | -38.91463 | 2026-10-09 15:58:00 | NPP-375 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f9b7cb0e-18f9-322e-939e-b20e34054047 | -15.25166 | -42.36578 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| e6c4fb0c-0e2e-3247-a420-585ccc1153d2 | -15.79133 | -43.38646 | 2026-10-09 15:58:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d1b1f6a-e09b-3d11-8d33-c9aaedac2d63 | -15.53713 | -44.40139 | 2026-10-09 15:58:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| ba847fbc-4454-3fc0-8e38-ed157a05dece | -11.57568 | -45.40579 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b630b8ba-bac9-3c67-a980-c5487cf03a9c | -11.87498 | -47.37387 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| bd0124b2-290d-3ab7-af93-9b83a6063cc2 | -11.9763 | -43.47026 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| af127400-8e54-3d7a-a89b-060d35da7897 | -11.82786 | -43.60271 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa3194ca-7533-33cd-acd9-6ce8a3950e97 | -15.25706 | -42.37572 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| c59e7794-43e7-37f1-869f-826504cb0a60 | -16.06951 | -45.26175 | 2026-10-09 15:58:00 | NPP-375 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| da5f35f5-ae36-3c24-80f6-395b9b1d58da | -14.53743 | -41.00073 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ba061531-7fd7-3425-a518-cc36a9305bd6 | -14.65009 | -43.53012 | 2026-10-09 15:58:00 | NPP-375 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| bd5f84c2-b941-3a21-8a71-da1737a875fa | -16.2244 | -39.14354 | 2026-10-09 15:58:00 | NPP-375 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 74343ff5-0446-3ba1-8899-325add56b9ea | -14.05168 | -44.80962 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 21938b84-5850-3159-8cd8-471f7bf0c96b | -11.95843 | -43.46627 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 00696282-482c-3a61-8d31-f75b97d600a3 | -14.06639 | -43.83607 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a1060a17-e6b0-3947-949e-983c010a20f2 | -10.81273 | -40.22839 | 2026-10-09 15:58:00 | NPP-375 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7e426270-2c90-3283-ac62-86f3266fb048 | -15.26488 | -42.38292 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.9 |
| 055fd957-167a-3419-a061-04adeeca245a | -15.10474 | -43.6358 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 56.0 |
| baeb6535-407e-33d7-8741-305dfc7bf572 | -12.82321 | -44.64474 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5433c5ec-2908-3446-a9c1-a2ab3b67eee2 | -11.90038 | -47.38536 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 68bb1c79-f3a7-31bc-84e8-6d68db43a77d | -11.57528 | -43.70198 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9f3e17ca-86cf-3079-9dca-2a82ed82b62e | -11.59698 | -43.63694 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d987a2ca-7eff-3dae-ab4b-a88528e784f1 | -11.83605 | -43.52471 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e464c4eb-ce46-3355-935a-25cb4a525253 | -18.08345 | -42.26765 | 2026-10-09 15:58:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 407e4090-e164-32d7-a96e-9faa968471fe | -14.86036 | -43.90809 | 2026-10-09 15:58:00 | NPP-375 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 16d0aa62-c52f-3d12-af0c-67ee13180c86 | -11.58218 | -43.66296 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 07f28877-d095-37a1-927b-ce79b00096f8 | -13.74703 | -40.83661 | 2026-10-09 15:58:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 109.5 |
| e071801b-682a-3d57-a1c3-b02dea67bdbe | -11.60659 | -43.61959 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 66dd5f0d-4c97-3610-924b-9521f80df5fd | -15.97 | -40.69542 | 2026-10-09 15:58:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f5644ac4-4436-39e9-9ffb-58d4c2f67c2e | -15.44491 | -45.56276 | 2026-10-09 15:58:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 794489d7-9947-368c-b027-3b270025c721 | -12.80332 | -42.47509 | 2026-10-09 15:58:00 | NPP-375 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4e303b45-c03d-3b5b-8236-fa276eba2762 | -15.26342 | -42.38253 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| 4e10945c-0128-3f9e-8ce6-02d94924fc31 | -16.83242 | -41.03555 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d34c197e-dc0c-3335-9eb9-f36c568feb8f | -17.84509 | -42.17217 | 2026-10-09 15:58:00 | NPP-375 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 8abd349d-7f7b-3540-b506-79def05240ca | -14.44713 | -43.92663 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 37.7 |
| fb3e403c-8d26-3f4a-9bc7-c399b689729c | -12.04204 | -43.3806 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8b33a615-08f1-3a32-9546-f973f9ea5efa | -11.98875 | -43.47725 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ef3e55c1-a93b-3d30-9a75-3735854d5d82 | -16.94513 | -42.08033 | 2026-10-09 15:58:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 76f47a7d-e2ba-38b0-90e9-b1c3126623e8 | -11.57577 | -41.41444 | 2026-10-09 15:58:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 5ea34cd2-46d3-3a3f-a7ca-646ebdead6cf | -15.06275 | -41.79737 | 2026-10-09 15:58:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| d121fd23-2d56-3418-875e-9cf8d2fa70b0 | -15.10522 | -43.64033 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.8 |
| ffcd378a-a389-31ff-a010-8fda2ac4abee | -11.58596 | -43.64629 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 392.2 |
| 95612b30-a60a-3b9b-ae39-3c10d443b1ae | -12.02609 | -43.44061 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1e952964-dbe7-3581-b4fa-bad6836aabc2 | -11.97247 | -43.48641 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| eec4cba4-f0be-3989-861b-e8994bc4737c | -18.00451 | -44.30474 | 2026-10-09 15:58:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4f1c092a-dd88-3d1f-b3b9-de323832056e | -12.0425 | -43.38443 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 53c04fc7-02fa-3c4c-97d9-ff08b999bf76 | -17.0979 | -40.76824 | 2026-10-09 15:58:00 | NPP-375 | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 2258368b-8a11-3699-96b0-3915a94da8fb | -11.99772 | -43.45599 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 37e61f3a-0e49-36b8-882b-91e9f0557755 | -12.00805 | -43.44588 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3b555c2f-aae1-3e1f-8dc6-a529b1c75760 | -11.28151 | -41.12715 | 2026-10-09 15:58:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 61.5 |
| bac15ebc-3cc7-34dc-802a-331f84f0d8cc | -15.38905 | -41.91172 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 204.9 |
| 23b4b389-a5cd-3ea5-8098-feaf3b464003 | -15.01989 | -46.25397 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2ecc33a8-abc4-3e90-9deb-5f468ef6e7ff | -15.01281 | -46.2541 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b4e52e14-45af-304a-886e-8e5cd527f2ac | -11.59355 | -43.70771 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| dd9dba4a-298c-3ab3-bc85-34beda134813 | -15.85389 | -42.02536 | 2026-10-09 15:58:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 410558cb-0b24-35a5-8521-7ce8b78470b0 | -14.64959 | -43.52573 | 2026-10-09 15:58:00 | NPP-375 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 08107ab5-7bfe-3327-acec-443c8ef6d7ac | -14.56157 | -41.1575 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f1d1c3e4-39ac-37ab-ab9c-a55ec5176f3c | -17.2976 | -41.21626 | 2026-10-09 15:58:00 | NPP-375 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| fc0727b2-b0ff-3d85-a918-0cedf6e905c6 | -14.59758 | -41.28363 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ad3a5aba-5cbe-37a3-adf3-5ea5a46f09f5 | -14.74254 | -41.15038 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1f12c822-aef1-3130-9495-f058843f9d82 | -16.1229 | -42.84995 | 2026-10-09 15:58:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f53f2068-393e-31f8-9346-ed70d51d95f5 | -12.03531 | -40.04016 | 2026-10-09 15:58:00 | NPP-375 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 2284fe48-cca9-34ef-9505-abdefcd8c29f | -11.83794 | -43.58931 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8d078225-af29-30e8-89d7-8346871404f3 | -15.93814 | -40.72796 | 2026-10-09 15:58:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| e20e95ac-0cea-36cd-9be7-aa5db243c9a0 | -12.29406 | -47.05865 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 097f6856-996d-3582-8eb9-2174f51a6509 | -11.5819 | -45.40876 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3a1cb0e7-60ed-3b41-b814-1a5d3769bb5d | -11.97055 | -43.47066 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 50f3e5bc-0fb6-39d9-a453-b72e48c8f6a9 | -14.05534 | -44.79637 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b98d1c70-6dda-3557-9724-ddbbfc9e8fed | -15.38491 | -41.92326 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| af4355f2-311f-3829-b7d9-c9b55ea86feb | -16.26884 | -44.17901 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3f6a4dcf-5378-3135-9f72-81c040482825 | -15.07384 | -40.16039 | 2026-10-09 15:58:00 | NPP-375 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 57e20ba2-04df-3d82-b9d3-ef6bc963a7cd | -11.59385 | -45.39373 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 94bedb97-f516-3515-948c-4fa5b35083da | -12.70227 | -43.0791 | 2026-10-09 15:58:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| e06383ee-f3c1-3cbc-a22e-17878514d6ca | -15.37132 | -41.89999 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 027d55be-70dd-336d-8a15-47409feefc75 | -11.59122 | -43.64169 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 320b4e70-28ca-3093-a716-25ff1c2e5714 | -14.04953 | -44.8022 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c41c294f-278f-3ef1-9a9f-5bda8e759f31 | -14.92642 | -42.00338 | 2026-10-09 15:58:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 47.5 |
| a195ca42-c9cb-3387-81e5-b702b31db344 | -14.54692 | -44.90897 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 144f988c-f970-3c32-93c2-5423a5b7bb80 | -11.58547 | -43.64231 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 84da14ff-6c0a-37b4-8dc7-386bd99cba42 | -12.254 | -44.75364 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0a5654ed-2ea1-3acf-8317-dfdd8d1fc355 | -16.24335 | -44.05368 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 8cf12533-2afb-3ed4-b20a-235592e5ba09 | -14.06171 | -44.78218 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1add095b-c9c1-34b4-8e57-f81cda50f6dd | -15.6902 | -40.72959 | 2026-10-09 15:58:00 | NPP-375 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| b6c48f73-e796-3160-b773-748f94b2c244 | -11.98219 | -43.46132 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| ee732ec2-9071-3b94-bf6c-0e302cf00aa7 | -12.1997 | -44.82997 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 4cb8edd0-d627-3303-9610-c06fa3119e40 | -14.0531 | -43.84775 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7b804509-79f0-3c0b-b476-ccd3d5d834f8 | -15.38207 | -41.89852 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 559e93e8-c999-337e-ac5a-d45cdbcb154c | -18.31819 | -42.37383 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| a3696830-872d-398f-8c3a-86345f7f1bfa | -11.79994 | -43.17719 | 2026-10-09 15:58:00 | NPP-375 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6b63436f-894f-35f6-87ac-85405e60b5e3 | -11.60272 | -43.6362 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e2f38deb-53b2-3721-9741-b4e9dcbfcad2 | -12.19073 | -44.64224 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e34cc957-8431-3cc6-a94d-c53e05b47a9d | -13.42286 | -40.96502 | 2026-10-09 15:58:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f72c080d-6b85-33dc-b388-23d1d40a8d08 | -11.58217 | -45.40564 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| fa40d585-2b2b-3a26-a3c8-9802367171bb | -15.0172 | -46.25293 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 84694d02-f2ed-31d8-b92c-f8e50e2ad823 | -11.98615 | -43.4956 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README261.md)
