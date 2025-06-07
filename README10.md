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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29dc7041-0d1b-3aaa-a6fa-1590c8791841 | -8.21006 | -48.98147 | 2025-06-07 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f89da93-72e7-3eb6-bafe-4d43add94eae | -7.72384 | -44.16589 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4dd89c8e-a64f-3113-abd7-d5ce407c5e60 | -9.40031 | -48.43636 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72d51957-5afb-338f-b81a-eab2a159d97f | -7.7137 | -44.17577 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76410e8f-410b-3684-87e1-70873b44cb0b | -7.71846 | -44.1727 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba6a37e8-74c9-38a9-9c67-6f242c2958c2 | -13.33885 | -45.48796 | 2025-06-07 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbb44d90-6ce3-3ebd-846c-c068a29943a3 | -21.3556 | -44.74912 | 2025-06-07 03:57:00 | NOAA-21 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a7d1f64-7971-3b16-b581-b842cbd96c72 | -20.9218 | -49.0951 | 2025-06-07 03:57:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 99b16f78-b828-3eef-a516-634485fbc281 | -20.90158 | -43.81981 | 2025-06-07 03:57:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 065fc475-b789-3aea-9400-78e8404baf05 | -13.09405 | -52.29006 | 2025-06-07 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ba416c8e-11c3-322b-974f-ee8d387c7d0b | -15.75907 | -41.4912 | 2025-06-07 03:57:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d7f36166-618d-32b2-a0d8-7d6dcd263b61 | -14.23505 | -45.49404 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 201688f0-5098-31b8-83e2-84497b1fef55 | -18.23667 | -47.94273 | 2025-06-07 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a5e362e-bb81-31a9-90a5-cb2bcb04d54b | -16.06487 | -43.65271 | 2025-06-07 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dea965a4-6964-3350-bf49-a051e83a7e2e | -20.90107 | -43.82071 | 2025-06-07 03:57:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76125b2b-b289-31c9-a77a-dfd8acb7597a | -20.9259 | -49.05032 | 2025-06-07 03:57:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1a9cc62a-e6dd-3e33-8059-bd427e74075d | -17.26288 | -42.65813 | 2025-06-07 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a4a95b79-6380-3d9f-97db-b56122fd5c67 | -20.59988 | -51.61157 | 2025-06-07 03:57:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a022a509-b664-3ee6-a993-3fd4734c50f9 | -14.22088 | -45.48012 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb2958a7-7055-334d-b56d-0d1f24ebf2af | -19.0804 | -53.46227 | 2025-06-07 03:57:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8834016e-17d8-3150-a85b-70fc208c5d57 | -14.73226 | -45.08189 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24a8af19-03dc-3676-a54e-04c3d7ec80e7 | -14.74304 | -45.08927 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fab9a676-5f5f-3675-9000-2ed35d779975 | -12.87804 | -52.20405 | 2025-06-07 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c942b6a-4a32-336a-bb86-f9a30faf2469 | -17.27027 | -42.65552 | 2025-06-07 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fafc3860-0a13-3e90-9ff2-d9936607cea0 | -20.76333 | -46.76783 | 2025-06-07 03:57:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6b2c2827-5a57-390e-a8aa-b0cc736cbdaf | -15.08078 | -48.94575 | 2025-06-07 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9eea6df0-190c-332b-a16b-318fca45b923 | -14.88102 | -48.11446 | 2025-06-07 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1529d1d7-63fa-3647-aa0c-d2a26650cf74 | -14.4997 | -43.80728 | 2025-06-07 03:57:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e108e14-e0a3-30f5-96ed-95e461ca6c47 | -15.91223 | -43.46034 | 2025-06-07 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61f52c5c-6782-3f27-80be-e060d824f1f2 | -14.73616 | -45.08265 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5f78a24-5097-383a-ac09-38ebb11143b5 | -14.73527 | -45.08767 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40707d15-13ad-38e1-a053-e60e4e034e99 | -20.9236 | -49.09292 | 2025-06-07 03:57:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b3ff1082-fefe-3cb9-8fff-9bdd973691dc | -15.38415 | -41.43074 | 2025-06-07 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 70a8123c-a0ee-3c70-b5ae-7c54a2061b4f | -14.22425 | -45.48451 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e60a649-00e8-3260-8e6e-0f55a64a13ed | -17.77945 | -42.81023 | 2025-06-07 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95e2b109-3fef-3da6-9afd-0e08138bb5ea | -12.88438 | -52.20536 | 2025-06-07 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f06e028f-c7c4-3931-80b2-fec6301d5bd9 | -17.27365 | -42.6561 | 2025-06-07 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65efe884-a067-38aa-a4b6-8979cb7462f9 | -14.23908 | -45.49479 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0116e11f-90ff-30c5-8e8a-d0dc8f1fd16f | -13.37023 | -54.26214 | 2025-06-07 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8be5ea27-b71f-3f19-b603-dc8284a27c1a | -14.72925 | -45.07615 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5985145-37a6-3a1d-b5bb-bbd3b2b80da4 | -17.1317 | -45.26579 | 2025-06-07 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70ec71ca-ae1b-32df-ab97-52516269e84d | -13.66337 | -47.70479 | 2025-06-07 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6782a6c7-d029-301e-963f-a36cefe3ef5a | -18.05776 | -39.91826 | 2025-06-07 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7cb98288-c51e-37ce-9515-5d0a86c8d0b2 | -14.90134 | -48.11633 | 2025-06-07 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee8942ec-5ea2-3327-ac5c-08f958082bd6 | -14.20014 | -45.50267 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8adb5ea5-ed4f-3439-a513-a4a1fa34832c | -19.07925 | -53.46737 | 2025-06-07 03:57:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92e24e50-1243-3294-ad6d-85bf6fab8d46 | -15.43448 | -41.41363 | 2025-06-07 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 265740d5-e343-34ca-9df8-6aea7e581dc9 | -14.21684 | -45.47938 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21c56a84-d355-3db5-89b6-2992a66c1628 | -14.74005 | -45.08343 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e58c8df0-df55-3869-83bc-bd6355ba12bd | -13.09083 | -52.28296 | 2025-06-07 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75dc54df-92f8-345d-9e34-f8b228f6d874 | -13.36314 | -54.26078 | 2025-06-07 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4961db92-8ea8-3b6e-bd85-76f8e64dfbdd | -17.81259 | -51.01112 | 2025-06-07 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e5aa486-baf0-3594-b663-0c2011d25058 | -17.63844 | -44.54237 | 2025-06-07 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3baa3cc7-d548-35c9-8cae-d09daeccd3b4 | -14.88667 | -48.11048 | 2025-06-07 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 412e0fdb-3770-3852-bb05-3c190251ae60 | -19.71749 | -40.35425 | 2025-06-07 03:57:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af8df3f6-a392-306f-8ed1-e651f1485a39 | -14.72837 | -45.08114 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54086d4b-1ab5-3915-9f93-03825d5bfb9f | -14.74394 | -45.08421 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c10b381c-eef0-3975-8f43-bd2da0447cf9 | -14.92817 | -46.00324 | 2025-06-07 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5abd9870-4564-3e95-b371-96c8e3bce4f8 | -14.73916 | -45.08847 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bbe6a00-7531-38f9-be88-8a42a21b753d | -17.02441 | -50.29941 | 2025-06-07 03:57:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285f6cbc-80ce-3711-9ac3-5dd2d1ba7d81 | -15.83862 | -45.69748 | 2025-06-07 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9976f538-581c-39c9-8993-9f407cf11ea3 | -14.92607 | -46.01493 | 2025-06-07 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9787414c-6199-373c-b7e7-e62d24e310ff | -20.92261 | -49.0978 | 2025-06-07 03:57:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| accfd19b-8191-3bdc-9f0f-70dc1794a140 | -14.2236 | -45.48817 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c22b915-f6b8-30e4-a93a-823ec3533a1b | -13.09717 | -52.28427 | 2025-06-07 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abee1ef6-2301-35a8-9a93-5bec8bf22e4d | -13.0897 | -52.28831 | 2025-06-07 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 324ea0de-bc3c-3304-9c1c-1795b6e79943 | -21.35209 | -44.74843 | 2025-06-07 03:57:00 | NOAA-21 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c0ac166d-57bd-32e0-a3bb-d206aa5b03a4 | -14.74605 | -45.09511 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ec3ea63-5699-3fe8-837e-a68026676e41 | -14.92747 | -46.00713 | 2025-06-07 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca1dce8a-ea6b-3689-aee1-1b238d06cd9f | -17.26627 | -42.65873 | 2025-06-07 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0265165a-39cf-37a0-8a12-10d06e723502 | -14.2008 | -45.49903 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79d3255a-5d5e-3c59-9bd9-57c4cfba1db8 | -18.23754 | -47.93824 | 2025-06-07 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd174b6f-9d0c-3e70-ab46-aff1885cea9b | -14.88241 | -48.1127 | 2025-06-07 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecf6d491-208a-3517-a9e1-926fc21e1ab0 | -14.2357 | -45.49039 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bd71bd7-f415-3ff3-84f4-ac75e16b7b61 | -14.72536 | -45.0754 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b136bea3-aaf7-3f82-b969-5678a82fd9d1 | -14.74514 | -45.10022 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d674fa74-bc90-3789-b0a5-b01e18dd6cad | -14.88704 | -48.11414 | 2025-06-07 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5355fa9b-5eec-344d-b837-9a5b238ac532 | -18.95889 | -45.38236 | 2025-06-07 03:57:00 | NOAA-21 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdbfa857-94be-33f8-93b1-f0a9673b8fbb | -16.03763 | -43.72594 | 2025-06-07 03:57:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e96e799-e37c-3133-bdf8-825429ec48a5 | -14.74215 | -45.09432 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc948a14-3dc5-3144-8898-d2dbd0dc3079 | -14.23635 | -45.48673 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef71a796-89d6-3ee8-84ac-3ff2a63b3d30 | -14.22022 | -45.48377 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf523132-bd48-39b3-8b0d-807dffa85be4 | -14.72447 | -45.08041 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7b1c712-9b32-3386-9882-7a0cc77a1a64 | -14.21956 | -45.48743 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8412a9b-2f9a-344c-a155-24500aef9e5d | -14.92678 | -46.01102 | 2025-06-07 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20fd757b-0b53-3cb9-863f-25cd439b63e0 | -17.78283 | -42.81084 | 2025-06-07 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de300bb8-a4a8-3263-a0e5-43202d2c6cd4 | -16.06842 | -43.65334 | 2025-06-07 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95b180ea-6a82-3457-9a9d-ae825c923e50 | -13.09514 | -52.28468 | 2025-06-07 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2dbc1aba-075b-3e71-bf4a-adb900e7108a | -20.9235 | -49.04738 | 2025-06-07 03:57:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1668c273-f942-3570-9d05-96ee6120ef7b | -14.20484 | -45.49979 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98b121e-dace-33f7-a265-1db925ccb035 | -17.63769 | -44.54667 | 2025-06-07 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 30cccee4-8cdd-353a-a8f1-12934d1412eb | -14.20146 | -45.49538 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d332450-255c-31d3-a58f-1fdf97a03c31 | -14.73138 | -45.08688 | 2025-06-07 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 654e497b-e0e7-35e3-a8c7-4a119dbe53b1 | -17.81184 | -51.01466 | 2025-06-07 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6481d76-ca40-330b-a59a-58d6f052ae83 | -14.20418 | -45.50343 | 2025-06-07 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3b91ada-c279-3524-9294-63869fb8a258 | -17.80645 | -51.01349 | 2025-06-07 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a30065c-d145-399a-96c2-c04f421f7af3 | -20.41827 | -43.55438 | 2025-06-07 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b33319d9-11ff-39e2-b777-020742828034 | -18.8204 | -46.43748 | 2025-06-07 03:57:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90667ca3-9c29-3615-b83a-fbc015f5b784 | -17.27089 | -42.65176 | 2025-06-07 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 420d068e-abad-3e2a-92d4-f67279015488 | -20.92255 | -49.05207 | 2025-06-07 03:57:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
