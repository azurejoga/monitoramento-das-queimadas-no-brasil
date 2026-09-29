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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82cf7052-3ed8-381b-b6d2-08d661bbf69f | -15.63657 | -52.68954 | 2026-09-29 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d2a99be-2df6-3b7b-9c87-f5b1d717a26a | -17.10234 | -43.20333 | 2026-09-29 04:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 644e0cdc-a167-37a7-9b79-fa7fc15e1efd | -15.17947 | -46.12871 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1235195-d251-3bcd-bef5-b06c89b5f39f | -14.63208 | -52.13363 | 2026-09-29 04:53:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0553c024-f83b-33f2-9032-b5b875dbd2e8 | -15.39142 | -47.90974 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8d99b79-46a6-3a82-9863-9fa1384bb871 | -15.15417 | -43.61668 | 2026-09-29 04:53:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97e9fd65-02f1-3e7b-9c98-1753d5030278 | -14.51185 | -48.29806 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11c32874-f603-3d8c-bc9d-ed50ab886938 | -15.16176 | -46.16685 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e24dd9a-7cbf-31e0-8a52-25fe7e8650b0 | -15.24841 | -43.26719 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 75beca1c-f303-3633-b724-fad252e015e3 | -17.55192 | -46.54385 | 2026-09-29 04:53:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33ed3d40-6653-316d-9e9d-2abd7f505257 | -15.12932 | -43.61866 | 2026-09-29 04:53:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33167063-5961-3022-a8a3-b62d3d8a226e | -18.56878 | -48.42514 | 2026-09-29 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a9442f2f-b856-3572-aa21-4a6daed0d7a3 | -14.21828 | -48.50951 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ea84da35-776f-3ab4-a7b6-3c00daff3026 | -14.44758 | -47.76329 | 2026-09-29 04:53:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9db2827-63b3-362e-83c8-1296ac0af25a | -14.50706 | -48.30584 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c9870ed-5cf6-35d7-81ce-2fc93bcaa5a5 | -18.68641 | -48.62884 | 2026-09-29 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c437f7a3-92fd-3ba5-8e70-2e00ff4e7afd | -13.89069 | -53.6803 | 2026-09-29 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4ee7cc21-88ce-3e0d-a4d8-79943f5e6f4c | -17.97757 | -44.48778 | 2026-09-29 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18fae8c2-a909-395c-81b5-63b7dab02c71 | -20.21173 | -48.56421 | 2026-09-29 04:53:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 098040c4-0990-3866-8510-1fea973b4bdd | -20.01162 | -48.31182 | 2026-09-29 04:53:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 647a1da1-b469-3485-a669-88fee00fda65 | -14.51971 | -52.48484 | 2026-09-29 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47258491-d81b-3056-835e-4e97f535afa6 | -19.53654 | -42.92788 | 2026-09-29 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ab46ea68-9ec4-3807-8ce1-59d4b249244f | -16.19578 | -42.87515 | 2026-09-29 04:53:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf769015-9710-36e3-8a2a-c2e3fdc64282 | -18.67902 | -48.62764 | 2026-09-29 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a92e457a-ed04-3337-bcb8-af43247a3fe3 | -15.47097 | -46.13364 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 339c8528-01ad-3c8e-a29d-51f8cd619a0a | -15.38646 | -47.91824 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86f6f53d-58e4-3a68-a4d3-9e30654384ca | -17.65641 | -46.53429 | 2026-09-29 04:53:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ca38f47-f6d2-322d-899c-7ff91ff75e72 | -19.53906 | -42.92884 | 2026-09-29 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5edc6af4-88d2-3b36-8771-224b65f23163 | -17.13855 | -47.72264 | 2026-09-29 04:53:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25cdad7a-89d4-3072-a167-e4cbe2286e3f | -18.48716 | -45.1263 | 2026-09-29 04:53:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5225f21b-26f6-36c6-8e1e-c7bbd35c3c0c | -14.09978 | -54.29828 | 2026-09-29 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f780bde-5982-30ea-9b2f-369a6a39225e | -15.23779 | -43.27164 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5478d89f-493b-3fb9-a497-623795e70cd2 | -16.34739 | -42.57094 | 2026-09-29 04:53:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fd9ddeb-cbec-3cf4-93b3-b163ac4d03ba | -15.39998 | -47.92951 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2648d08-e87c-3be6-a823-6142ebcf825f | -15.7765 | -52.45354 | 2026-09-29 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c9a2f8e-523b-3913-86ad-8b80b8d69d4b | -14.77081 | -47.15519 | 2026-09-29 04:53:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 447f3660-c8e0-3e31-bb4d-abc182611666 | -15.2218 | -46.17501 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d31ed84d-94ca-3183-83c2-933c7c9605c6 | -17.25874 | -48.28491 | 2026-09-29 04:53:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 709d4a87-73b2-3222-a46f-51c48c499b2c | -16.75955 | -47.07287 | 2026-09-29 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdf2ced0-910a-3bf2-93a2-eb73a3211425 | -15.01236 | -51.40411 | 2026-09-29 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c106951-59c6-3b34-b149-ff3435da52dc | -15.39629 | -47.92892 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09a6b577-2d20-3930-9a97-5a8eb2af6e1f | -15.25622 | -44.82159 | 2026-09-29 04:53:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c2b9af3-8a71-37df-9982-5748cd2682aa | -14.09184 | -54.30127 | 2026-09-29 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdd125cb-f045-3b42-bbc3-cc4b7491df39 | -15.93441 | -42.33471 | 2026-09-29 04:53:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b00149a6-bae5-30b3-a26b-ec60cebc6101 | -18.56505 | -48.4246 | 2026-09-29 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| abfedd1f-2134-33b2-84c3-9a5d68f9f6b1 | -14.37008 | -52.13736 | 2026-09-29 04:53:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1a8cae5-ba76-3831-8b94-0c527b53b772 | -17.65178 | -46.53754 | 2026-09-29 04:53:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1bab4ef-6c2c-3b31-a375-a522fa6281fb | -18.49576 | -45.13208 | 2026-09-29 04:53:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd34851b-1dcc-3a52-9612-4a908f012265 | -15.45134 | -49.07438 | 2026-09-29 04:53:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0c3e1c4-ba97-334a-9ffd-79538fef30b2 | -14.22278 | -48.51181 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43445cee-977f-3a94-bc00-d7d729c66f2c | -18.10504 | -44.35305 | 2026-09-29 04:53:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fd7d7f8-78df-3621-a202-477384c0c905 | -16.35078 | -42.58789 | 2026-09-29 04:53:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 406c04e2-d1e0-3a78-85a8-ac90fe706c41 | -19.75874 | -48.93485 | 2026-09-29 04:53:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89701bae-c6b9-3ea2-a0be-9375962c3f45 | -18.08848 | -44.36905 | 2026-09-29 04:53:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8b5d8cf-2483-3cff-a86b-d43d6a1b5b76 | -15.18765 | -46.12997 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eef01be6-87d6-3bb7-9b00-fd5e5c00be00 | -15.82909 | -42.56182 | 2026-09-29 04:53:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8da6f7cc-2e35-3dbe-8edc-69e58ac2c20e | -19.53867 | -42.93242 | 2026-09-29 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| efee30f7-5863-38bc-85c2-e346c94e9be9 | -19.18699 | -46.81223 | 2026-09-29 04:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ac78536-a2ef-3e17-82da-36b8359a3609 | -17.10335 | -46.47139 | 2026-09-29 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1bc2657-64c3-34b8-a337-6689db0bb052 | -15.46086 | -46.14662 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dce924d2-3eb2-319a-8053-abefd735be5f | -16.23029 | -48.06596 | 2026-09-29 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2f6ed3e-2dcd-3c6d-8b3c-6d6b1a714f74 | -19.36852 | -41.50294 | 2026-09-29 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 095ede35-b349-351f-9d7f-f101a84cf940 | -15.24276 | -43.27232 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 214ada40-0cc9-32bb-9c33-1e30cf093288 | -14.9626 | -47.54128 | 2026-09-29 04:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddb4bea4-b6fd-36c7-8a10-564189741234 | -15.95813 | -42.95768 | 2026-09-29 04:53:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4af737af-0c30-3f16-a8a7-5a755a0087c3 | -17.13713 | -47.72021 | 2026-09-29 04:53:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99d25bf1-aa8d-3214-b65e-5283a03f061e | -18.0933 | -44.36938 | 2026-09-29 04:53:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb78e0db-4152-343a-9a2d-af90067dda4f | -15.77315 | -52.45296 | 2026-09-29 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be6dfcfe-7243-3eee-bc7d-afddfc5ac220 | -15.00846 | -51.40714 | 2026-09-29 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6724407a-f933-329e-a083-b9613e6236f5 | -14.10485 | -54.2904 | 2026-09-29 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f85fcce-a3f5-3ca9-8cf2-2c4c0f8bb9e0 | -15.87046 | -40.45339 | 2026-09-29 04:53:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 53f97ad8-7610-3b22-a9e2-733c71bbbddf | -18.56131 | -48.42407 | 2026-09-29 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fceabd20-497f-3923-b264-419a65f74723 | -14.79683 | -45.957 | 2026-09-29 04:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a6a893b-93b5-3ac2-9961-92503240ed06 | -19.53365 | -42.92861 | 2026-09-29 04:53:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9e59a7c7-54f2-3d6d-9993-001a468c9f9f | -20.21551 | -48.56479 | 2026-09-29 04:53:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b76fcd9e-13e7-325c-916e-ec4dc9cfd9e0 | -14.75574 | -51.39845 | 2026-09-29 04:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 713b06fd-08bc-3a99-b727-6b1e5d722a65 | -14.21631 | -48.5066 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afcb51a3-f0ce-30bf-ab18-44c3ef6015f0 | -16.41271 | -51.86662 | 2026-09-29 04:53:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1224234c-414a-3194-9a13-3f052cad86c1 | -15.09437 | -53.87093 | 2026-09-29 04:53:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad21b378-2b1b-3199-9012-3f35738e70d2 | -18.09971 | -47.89694 | 2026-09-29 04:53:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76b3cf44-9ab0-3ef7-bceb-0c538c0ee841 | -14.53935 | -48.31081 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 636cfeda-779d-387c-9d28-67157aae766b | -14.51966 | -48.2949 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa84cf2a-d00e-390a-a853-fafb38a38e6c | -14.97066 | -46.26429 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c41b3371-78f3-3b28-a94e-2695d182a80a | -17.80515 | -44.43068 | 2026-09-29 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ab69a33-136a-35a5-b526-8ebbbb3f4709 | -15.2146 | -46.16644 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff139896-f77a-3dd5-9cb0-84ebea08880e | -14.86108 | -47.98956 | 2026-09-29 04:53:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b503204-1f6b-3dba-80a8-959ea161b806 | -15.24624 | -43.27806 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 0e9942e5-7c90-3819-b0e0-3c39a9df0e9c | -15.21872 | -46.16677 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed22eff0-eaaf-338e-82d4-9afa2c1b876e | -15.38074 | -47.9197 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab90d15-bf65-3125-b58f-11237d4996d7 | -15.19383 | -48.43343 | 2026-09-29 04:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f53e97e-cfa9-32db-84c8-448d6a01af4f | -15.22493 | -46.18277 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce3bce81-5f06-3570-96cd-c89e02738e70 | -14.09544 | -54.3019 | 2026-09-29 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c17abfa0-3ace-374a-9945-9eb4a045ca09 | -15.3901 | -47.90729 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5db97cb-d274-31f1-a632-2b4094c361f2 | -19.18427 | -45.22021 | 2026-09-29 04:53:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 585613ab-5086-3067-931e-326047325da5 | -18.49635 | -45.12729 | 2026-09-29 04:53:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9de26349-4613-3a73-b7d1-998884ab6dfc | -18.39916 | -42.31311 | 2026-09-29 04:53:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 538cc0a6-2234-30c9-94c7-47ce476f7b82 | -16.69557 | -51.8371 | 2026-09-29 04:53:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f780c523-45b3-3e3d-8a80-794d05d42ec1 | -15.16991 | -46.16818 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c12a584b-115f-3c9d-bb38-cd8d2c838d73 | -15.38574 | -47.91126 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3bddaaa3-64ec-337e-90f4-92fed847281f | -15.2969 | -53.65766 | 2026-09-29 04:53:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README52.md)
