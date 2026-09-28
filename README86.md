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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c37f13e-8734-3c20-9f1a-60f810118608 | -11.52984 | -41.67171 | 2026-09-28 15:29:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 98763a30-a08a-3b1e-be30-5cc783201e34 | -3.97218 | -41.52827 | 2026-09-28 15:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 2043d52c-8196-36b9-854e-8c5450806ef5 | -13.71965 | -39.67247 | 2026-09-28 15:29:00 | NOAA-21 | ITAMARI | BAHIA | Brasil | 2915700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 54f0c1a8-d98e-3613-af44-917c1f2c7d8f | -9.34206 | -35.60568 | 2026-09-28 15:29:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fc21475d-97b5-3ea9-98c1-d6b903d9fa2f | -15.37071 | -41.32333 | 2026-09-28 15:29:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e6d289c5-321d-3833-af6d-3cacbc748ee3 | -9.18578 | -40.0488 | 2026-09-28 15:29:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 16d5d171-c81c-3f03-b8ae-09325763879e | -3.67507 | -42.67126 | 2026-09-28 15:29:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 3f6bae27-18c3-36dc-b870-77628930882e | -14.43869 | -41.79073 | 2026-09-28 15:29:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e51e9fe5-9868-37d5-94c8-4cb0db45bdb0 | -15.16787 | -39.82476 | 2026-09-28 15:29:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7fc083c1-f30d-3b8e-a2e7-3c7a11103b65 | -14.58482 | -41.23881 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 936787e4-7646-3167-b9e5-8d9d46c83dda | -14.74773 | -41.95731 | 2026-09-28 15:29:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 6b04a60a-f27e-3797-87bc-9ff9ed3ddd51 | -14.09117 | -41.38934 | 2026-09-28 15:29:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 104da6cd-b90d-38a9-9e76-2f35c10c9908 | -9.15863 | -43.07972 | 2026-09-28 15:29:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 79492984-abbd-31fc-9b20-c3897ebaf8b6 | -12.74742 | -38.16734 | 2026-09-28 15:29:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e10917ee-3159-3101-b7f4-b969a22f8c8c | -15.64665 | -40.4292 | 2026-09-28 15:29:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| a5a78c64-3b76-3b08-bee6-919b54e7b25e | -14.53449 | -41.27802 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 7a51b450-1cbe-3bbd-b032-4a2c239040c3 | -16.34779 | -41.8224 | 2026-09-28 15:29:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| ec048791-add3-36be-950f-f509b71e2b30 | -11.35899 | -41.49803 | 2026-09-28 15:29:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 6a4232eb-8f12-3513-ab89-1aa0ce4e8bd3 | -16.34261 | -41.81967 | 2026-09-28 15:29:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| cd1391d7-c29b-30d0-af9f-1bdab98d69f8 | -11.14991 | -37.6524 | 2026-09-28 15:29:00 | NOAA-21 | BOQUIM | SERGIPE | Brasil | 2800670 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e83c122b-f671-3521-8108-2c30da713f83 | -3.66918 | -39.00011 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2497ec3f-84ab-3627-8f67-dab8baf16f48 | -12.7573 | -41.55323 | 2026-09-28 15:29:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 81e316f1-ccb7-31dd-8631-935784f5fe00 | -14.7716 | -41.14168 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| ffaefa77-722d-3b49-b3a2-3fa54524e5ec | -14.43843 | -41.7867 | 2026-09-28 15:29:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 51702d19-60d6-32a5-a38a-8755d6a64b8c | -15.34407 | -42.16947 | 2026-09-28 15:29:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| d6244f22-37c1-37b2-a709-5afc4895f06a | -14.74957 | -41.95986 | 2026-09-28 15:29:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| d3d020e9-e89c-3e03-838b-4db10a443c9c | -4.00823 | -43.2295 | 2026-09-28 15:29:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0372b38e-548c-323b-a8b8-e9a2b460ef23 | -3.67108 | -39.04718 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7262709f-0d1d-30c4-b24d-a2e7d514a342 | -12.17566 | -40.73323 | 2026-09-28 15:29:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 405ea30b-a436-3f33-8a21-ff9eb11194fd | -11.05349 | -42.98527 | 2026-09-28 15:29:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5411cc2e-70bb-32d1-94e7-4e2dc8bc8aa2 | -11.70229 | -41.75227 | 2026-09-28 15:29:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1e251896-1978-30f9-a201-a348ec4d6321 | -11.05429 | -42.99238 | 2026-09-28 15:29:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| d53e3b9d-ebab-31f0-8b55-6a84d4bb1a59 | -16.28943 | -40.19849 | 2026-09-28 15:29:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| ab199282-d184-3b02-a0b7-0c8943a5a163 | -14.10271 | -40.72182 | 2026-09-28 15:29:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 21aec743-2c1c-37fb-9349-eecf4d07124d | -3.66855 | -38.99741 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 95fad967-d594-38bf-86bf-8fe07cb56ed6 | -11.43902 | -41.98418 | 2026-09-28 15:29:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8ad276f5-4cb4-3058-bba3-6624b05fe821 | -15.42877 | -39.09618 | 2026-09-28 15:29:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| 5c46e752-3dbd-330c-9727-0e2166acdb4d | -15.44634 | -41.44352 | 2026-09-28 15:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| c0204029-50cb-3538-8dcf-d19b4b7683c3 | -11.32104 | -40.34618 | 2026-09-28 15:29:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| fcf7142c-cec7-3f2f-8094-d2798ce87ed8 | -12.70377 | -40.55566 | 2026-09-28 15:29:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c58444b5-0803-3d2f-a5d0-f3547100b788 | -8.68592 | -38.195 | 2026-09-28 15:29:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| ec53927a-900a-317e-afca-ff1d43c9d449 | -15.45325 | -41.44342 | 2026-09-28 15:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.5 |
| 87da6768-d874-3fa2-a86d-c14d0566fa00 | -13.3319 | -39.2035 | 2026-09-28 15:29:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| affb0a5c-c675-3692-87b5-480ef3bbae82 | -10.27039 | -39.58698 | 2026-09-28 15:29:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c62919d9-caca-3127-b82f-d42463e7019e | -14.7783 | -41.14108 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a67cfb3e-ebbe-386b-a0bd-6d1ddad2e0cc | -14.09515 | -41.38976 | 2026-09-28 15:29:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 5c194537-76cd-3dcb-8425-bdd008ccdcf8 | -6.61489 | -43.73516 | 2026-09-28 15:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4c8a1824-8d0e-3325-8c26-17bca24f3edf | -14.15497 | -40.65769 | 2026-09-28 15:29:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7c2b95b7-c0a2-3cba-a1ae-0a589fcf620f | -12.26114 | -42.19143 | 2026-09-28 15:29:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4ca853b2-30ac-36bd-8106-51b9970f6f08 | -14.13107 | -40.67912 | 2026-09-28 15:29:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9822acae-57b6-308a-ba5d-ca20f2d2705f | -11.52317 | -41.67237 | 2026-09-28 15:29:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| fe56a67f-a190-3f5c-b08b-4bb47c49bc70 | -14.86525 | -41.0275 | 2026-09-28 15:29:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 1d0ede28-02ea-32d2-9569-a4b4e46d7769 | -3.87863 | -40.83456 | 2026-09-28 15:29:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 39ff1c79-6539-3894-95ed-5dc58815dd6e | -14.10219 | -40.71663 | 2026-09-28 15:29:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7a94571f-7abd-3181-b933-cef55b4c3fe9 | -14.55908 | -40.74263 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 76019b75-8856-3504-a876-3d1de9b5843b | -5.1906 | -36.86958 | 2026-09-28 15:29:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 909337e4-7bfd-3324-bc0a-7b83e87877b3 | -15.44758 | -41.44355 | 2026-09-28 15:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| a50f3518-e6c4-360c-bf68-7c4f2a591edc | -14.45348 | -40.80637 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 182a01d9-dba7-3135-ab20-4a2c5de6f7e0 | -13.33215 | -39.20378 | 2026-09-28 15:29:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 69d0b868-806d-3f72-80b8-79a91ea75970 | -15.42517 | -39.09708 | 2026-09-28 15:29:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| eec3b346-c34e-31aa-bb77-e88b6b87e8ec | -14.2369 | -40.94479 | 2026-09-28 15:29:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 414d00bf-83ae-333d-996d-5df8ebb180d7 | -14.73153 | -41.37436 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3b4907cf-1760-3780-946c-0148ae85541a | -14.5045 | -40.53958 | 2026-09-28 15:29:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 962839c2-b4bc-35bf-80e3-0f2031eb3abd | -14.52173 | -40.76404 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c935b471-b175-3ca1-9c4c-aae8f6d7d323 | -13.87312 | -40.80034 | 2026-09-28 15:29:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9b0a6009-9c8c-3854-824d-edea91450553 | -14.73519 | -41.04929 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b7f62ac1-ff25-3f0a-b799-f295b7261018 | -14.591 | -41.23299 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 275e904b-2630-3e5b-978f-e521efe63ff7 | -8.6996 | -37.06998 | 2026-09-28 15:29:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 68e07343-3fdf-33f0-b9dc-11754d698c76 | -14.64643 | -40.69612 | 2026-09-28 15:29:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 105.7 |
| 0c580a9f-4dc0-3404-a40a-434f37d8f66e | -3.88488 | -40.83748 | 2026-09-28 15:29:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 473ddfac-17c6-3916-8961-11be777872c2 | -12.82576 | -40.70067 | 2026-09-28 15:29:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 902efc3b-cbb0-3694-80c1-36b332b84087 | -15.34775 | -42.16675 | 2026-09-28 15:29:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| c3eb206e-2b88-36a2-be95-964366382b46 | -11.68662 | -39.81253 | 2026-09-28 15:29:00 | NOAA-21 | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d7fb9371-03fb-3c9f-95df-33269f8053a6 | -14.25406 | -41.28802 | 2026-09-28 15:29:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3fa429f2-a344-3c5c-ad5e-b9bfd03d0bfa | -16.35924 | -41.24856 | 2026-09-28 15:29:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 9948e93a-c02b-3aee-acc9-8f6f8de60074 | -6.73092 | -43.00802 | 2026-09-28 15:29:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 76121551-8d6a-3a3c-9599-8c440dfb8574 | -14.10121 | -40.71464 | 2026-09-28 15:29:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| dad23476-3aa7-38dd-897e-561adf74288b | -13.36386 | -40.96793 | 2026-09-28 15:29:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 4958e1bc-781d-3495-b51e-84f1398579a6 | -16.35003 | -41.61093 | 2026-09-28 15:29:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 2d79bd8e-32ce-33c7-b9da-aba2ac8d9e10 | -14.70079 | -41.8952 | 2026-09-28 15:29:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 63f7656c-d09b-3af8-b722-286d954dae4c | -3.67664 | -42.67003 | 2026-09-28 15:29:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f6dc5d19-e54d-3803-babb-0fb76ab3c69d | -5.73095 | -43.28141 | 2026-09-28 15:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fb02f4c1-c4b0-365b-b903-4034c62d6e24 | -10.0766 | -40.03144 | 2026-09-28 15:29:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a1ddbc5e-18d5-30bb-b2c0-60d4f65b7b85 | -16.35804 | -41.24723 | 2026-09-28 15:29:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 7f36bf6d-05b1-3501-8015-68be437a4bf7 | -15.08658 | -41.13495 | 2026-09-28 15:29:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 745b8069-6100-30e1-aa15-954a3084859e | -9.33774 | -35.60636 | 2026-09-28 15:29:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2d75764c-4117-38b9-a1c8-52d9b9f6c334 | -14.45392 | -40.8063 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| c50965f9-76e8-3937-9bcf-a1b8275edcc0 | -14.17746 | -41.8364 | 2026-09-28 15:29:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 852565a3-363b-3acd-9ed3-6345f99c415d | -3.55672 | -39.03595 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 88aed615-8912-35c8-ae2f-43950b728bbc | -3.66933 | -39.0355 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b2907da2-a2f9-34b1-8a69-76da06155f43 | -12.65639 | -39.2831 | 2026-09-28 15:29:00 | NOAA-21 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 0dcf5332-f4ab-39d2-a5bc-992bbcf57250 | -3.66875 | -38.99722 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 68265566-ec92-35ab-b999-131197e5b1ff | -3.67064 | -39.04424 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| c0c2a833-9c22-34f2-a256-cbe39f9b8701 | -15.20833 | -41.5098 | 2026-09-28 15:29:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| cc750d12-6d9c-3d5a-b7d8-580a84dc601d | -14.33505 | -41.38507 | 2026-09-28 15:29:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ab2ca439-28c4-3ca7-82fa-fb8d3528d42d | -6.58829 | -42.9352 | 2026-09-28 15:29:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 214c72d6-f38e-31a9-9425-f0073b635b73 | -14.80271 | -41.37896 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 338c81b5-e09e-328d-9bd6-41ec5435a908 | -15.08994 | -41.13532 | 2026-09-28 15:29:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 481e91c5-04f5-3c8a-bc1d-a65d7c76d270 | -14.50552 | -40.53515 | 2026-09-28 15:29:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 563a688c-e4ae-361d-8f3a-082c9008e6a3 | -14.64623 | -40.6943 | 2026-09-28 15:29:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |


[Clique aqui para ver as próximas entradas](README87.md)
