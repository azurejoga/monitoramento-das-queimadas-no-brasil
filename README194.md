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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45ef630b-4b09-3211-876e-9b0612b67531 | -8.13798 | -49.44055 | 2026-10-09 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f23c76d-229d-3871-bc6e-f0397581d0cb | -3.06066 | -59.26752 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e3c462f-1993-3232-a960-60edb592c807 | -3.60502 | -61.62808 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e6a532c-d11e-3968-ac61-70c478bf4616 | -2.43551 | -55.97126 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ad070ca-e55f-3e62-a8ba-4b56d6fa5b2d | -2.83291 | -49.51538 | 2026-10-09 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7743f09-d049-3b40-beae-a63e31bbe001 | -3.00009 | -53.90458 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 19a865d6-2676-310b-9d35-ae014db23bc9 | -7.00361 | -59.10603 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aff48596-2a79-388e-8684-1c078ef1500d | -2.99626 | -54.0815 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8228b8ce-4e88-38f7-ad41-6fa9645ffa82 | -3.08362 | -54.28969 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c171d268-e926-3310-958d-b90028f795b9 | -3.18654 | -58.64526 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d783d11d-bed7-3280-b5bc-ed18d78e604a | -1.77124 | -55.06216 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0dd8804-a3d0-38e0-8bd6-8f2022e6bf3e | -11.40546 | -46.67898 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| acebacb8-2223-3c46-82d1-bb6b9356c194 | -9.88652 | -50.48948 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deffebc2-0641-3476-94d4-dbd1a0cbdb1d | -3.65821 | -59.16245 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dd236e2-8d65-3463-a801-7b30193756fe | -3.64864 | -59.5654 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3317a094-27ba-34bf-9029-bd15b33da0a7 | -7.21704 | -55.08311 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 5c8d76ef-bc10-35b8-a36a-e22e86c479c3 | -3.34633 | -50.40526 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34364dd8-dbad-3164-a504-7450b737b2ad | -3.5946 | -54.56492 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc672308-84c1-3d6d-85b4-95c340089787 | -3.34868 | -50.42294 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 90916087-9f0b-3ef5-92d8-250e4f2f576e | -3.48711 | -59.38134 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83fb16c6-6d61-3f49-9251-fc117ac97019 | -2.23797 | -51.92845 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa88f65f-2b4d-3cc2-bac7-addc234a8058 | -3.93662 | -56.02333 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e3af98c-1a33-3bf2-b64f-0d07e20ecfec | -3.56249 | -54.66929 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f9f6c93-675b-3425-bf2e-1f80a5f823e3 | -1.54405 | -54.55854 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf3bb7e1-5dac-32dd-91ef-c38570aa7485 | -9.51145 | -64.35426 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43121011-9e71-3a3b-a59f-27efd07f797f | -3.03483 | -54.09936 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 229a16c3-8562-3ebc-ba76-aab7aa9b1a70 | 1.69909 | -55.6026 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22c43c27-9896-3f7e-b02f-3e1a176e082f | -3.51532 | -58.02734 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dc14fa8-b6eb-3863-b7b0-9c12a5604d1b | -4.56365 | -54.95858 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5d4878f-4f60-3da3-b00c-49dc83581c94 | -3.73917 | -59.42144 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f13de72b-de54-3856-a3bf-3a8666d234c3 | -3.32556 | -58.15264 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46cc713d-76b4-3c55-b8fe-3f0457b203ed | -3.44085 | -57.57447 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10ffb4b0-afbd-32e8-90ff-5fd392e1865e | -1.19491 | -54.20818 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2be2e61e-1ada-331d-8383-10ade680b538 | -3.91539 | -52.13916 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee1b8829-4260-38b7-a94a-0a83c03c215b | -2.22478 | -58.10937 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcd48b6a-b539-3e75-819c-0515d41d790d | -2.41709 | -56.53833 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 901037df-83cb-37ff-b12f-01e3c518ec6b | -9.29274 | -47.47068 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e8c010cf-5828-3f6f-841d-88d59aa0df45 | -6.92221 | -59.27752 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af22ccff-9a5a-3d57-b79d-868fab4ab2a1 | -3.56924 | -59.10183 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cb61889-bab1-3276-87f3-7951022ef195 | -1.48413 | -55.87143 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 826df596-0cb2-317b-9e54-f328537126ef | -3.25805 | -54.02959 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86639be8-59c6-3a1a-a844-b2810e7f8a40 | -3.47355 | -59.50857 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a78ad3a-ff0d-34ae-a071-4bde6de4c186 | -10.28479 | -46.61435 | 2026-10-09 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d63319f2-d131-3b44-bbdd-a42112ff8f4b | -3.10288 | -54.18431 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28b2453e-0251-3c4f-9ecd-5a2c47366484 | -3.54402 | -54.6895 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c2cd2238-aeb7-3c31-a8e8-5b3ed1542636 | -3.44826 | -60.27296 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a8043b8-b1f4-333c-ae58-d1ea0430f080 | -2.8507 | -59.26337 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22acf51d-b91a-387f-994d-8c90e33d2c56 | -3.45636 | -57.49805 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93a54636-4b5e-3ab1-8b5b-cbbc33d52c66 | -2.7354 | -58.19016 | 2026-10-09 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec52019-aa37-31ee-a817-1c07370596e4 | -3.28857 | -61.00816 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b893f60d-8f84-3404-a834-b448fcc7c1bf | -3.99886 | -56.25353 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a3b6a8f-1d5e-32f9-9762-15560b90ac61 | -2.99292 | -53.84775 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 72d7bd67-e9e5-326c-a59a-912f21f9ae29 | -3.08634 | -54.2682 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af395825-12e7-36ed-a2d0-3a791d8945a9 | -3.66882 | -60.53894 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0549b851-fd31-3b70-a0d7-35a7608ccbed | -3.78458 | -58.64479 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67a59613-3067-3472-9a83-cdaaffff86bf | -3.72617 | -57.1453 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b57e85a6-c646-3a4a-859d-3c7e2d1afde9 | -3.48476 | -59.45995 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b075d26-cdfa-30b3-afa7-3cc0f7f6ea0e | -2.52922 | -58.09752 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f6dae49-eb77-3d18-8ef4-d2a8c3377372 | -3.04569 | -59.36206 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6ae9a2f-b4c1-3295-ad0a-c38138ce39e9 | -2.30443 | -58.10115 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df0edd59-f01e-3960-a157-cde14e91fc34 | -3.74305 | -59.43998 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fced724-05b9-387b-8b0a-82a8865a16ae | -3.63935 | -60.63412 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f0f9b44-0239-386e-971c-267405464702 | -3.47411 | -59.50505 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79140866-f128-33ac-b586-beb72e99d138 | -2.62441 | -57.71002 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd97cc57-0036-3a50-92cc-dc6501135f59 | -7.22254 | -55.09895 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 789d89ff-ad9a-3c0f-97d5-3517d0e50926 | -4.37991 | -55.44772 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cda7dd92-6047-3ac5-a354-94bb76a45e34 | -1.25106 | -55.88215 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d645826f-2ca2-31a2-9c34-96530904618f | -3.77622 | -58.59061 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 744ce2e3-4893-3a59-a8d5-d03b29ac76cd | -3.7303 | -59.41286 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e94071f-1d55-3200-8ce6-440672d9e0a4 | -3.58789 | -54.58094 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 948bb270-ea15-398d-99c4-2274471a3b98 | -2.82859 | -57.62162 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfeeca48-ca5e-3998-9b7b-96e4cf5c1cca | -3.50714 | -59.34152 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fa145ec-eabe-310c-a480-3b8212edd123 | -3.29321 | -54.08426 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf2b2936-b3b2-371e-a9ce-f64192d4d8b3 | -2.5856 | -56.17538 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b188053-fe77-3d4c-90b8-ad6950393f7a | -3.18529 | -60.05621 | 2026-10-09 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5998653e-5939-365b-a9b8-fc5bfc9277d8 | -2.98931 | -54.07557 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55721abf-e290-33b1-8119-080153a28506 | -3.16925 | -50.59613 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8aa757d-6d81-35fc-8b25-e66c7cf262c8 | -2.85181 | -59.27369 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16b7363a-a14c-39f2-a881-a15d62342289 | -3.63806 | -59.56733 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e1d24b6-14d3-37cc-bada-e38f30e0f187 | -2.8996 | -59.23107 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f19fbf-7e18-39d9-8d25-b329c6075a06 | -6.68083 | -63.03083 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a83be051-2a9d-3794-951e-3fee1162fbab | -3.25564 | -54.01932 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32f6cb18-f481-32ec-9d73-56c723cf18bf | -2.86753 | -54.16044 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54f5b4b9-a431-3ec6-8a04-6c03a3fbf0d3 | -3.28961 | -54.00471 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0468071-9dfe-3ee0-8173-898283c709b1 | -2.47596 | -56.0744 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90e8a146-5583-3286-90b7-df76fe75106f | -3.03599 | -54.14325 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77f9d0e3-516a-3dc5-b288-8f127074756b | -3.74191 | -59.4685 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27ff362e-db59-35b9-85ce-412c633cb4b7 | -3.92961 | -56.02224 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d89f5ee5-895f-386f-b476-57e5d3630ede | -3.16996 | -54.73299 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfa83a8d-5305-3551-8c38-42f612d657ae | -3.69852 | -60.55135 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dfbd3aa-74a5-37f7-932a-2776b52126ae | -3.02138 | -54.05826 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0499bf7-b7d1-3222-a2e5-a4bb28c79f72 | -1.29043 | -55.69905 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e43610ab-923b-3f44-b0c5-82274cb72a4a | -3.97071 | -51.86514 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f6ea9c2-982b-375f-bd1a-a90e409237d4 | -4.16989 | -54.99522 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7dfbbf7-5e20-3bf8-ba66-e89ee90e3385 | 1.68845 | -55.62287 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c811782-cf96-322b-ade0-0d92d2ac98e2 | 0.69826 | -51.43215 | 2026-10-09 05:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a06bb8-25f6-3317-8d6e-6b6d033ee7c6 | -4.101 | -54.02335 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52c5fc5f-4f27-33a1-9bae-ad100110bdc0 | -3.08723 | -57.66231 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e43f46e-8f93-34eb-ae13-42c4802688fb | -2.88617 | -54.18539 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e474ead-d0c6-3a20-9a91-bb70c9ca4d35 | 0.69826 | -51.43214 | 2026-10-09 05:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README195.md)
