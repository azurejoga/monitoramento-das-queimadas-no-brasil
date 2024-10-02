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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84bfb4f5-8f6f-3741-949b-e0740b4deff3 | -18.96367 | -41.52339 | 2024-10-02 03:55:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9cf18d9c-5e09-322d-bbcd-8bde199479c3 | -18.82362 | -40.19647 | 2024-10-02 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13e75cd1-4413-3497-97ff-77fb90dfe6bc | -20.86143 | -41.67911 | 2024-10-02 03:55:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0c9d807b-2415-3068-b1b9-4b5adecedc50 | -20.85812 | -41.67852 | 2024-10-02 03:55:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6228edd1-de74-32b7-8a7b-8a590cda3691 | -20.85539 | -41.67425 | 2024-10-02 03:55:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 11f25543-b574-36d5-a2a4-d6bd64441ba1 | -20.85481 | -41.67793 | 2024-10-02 03:55:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a6abd9a-acc6-39c3-bac6-ad20e1905f0b | -20.69496 | -41.97966 | 2024-10-02 03:55:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 272811bc-bb45-369c-8c32-059fa101d824 | -20.63925 | -41.98859 | 2024-10-02 03:55:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 57f35414-707e-3267-aeb4-2b5f0f1464ef | -20.59422 | -42.0145 | 2024-10-02 03:55:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44e4dcbe-07a5-3ad7-b66f-06ba5a82e56c | -20.35746 | -41.66708 | 2024-10-02 03:55:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0513bf5f-39de-34b3-9809-e5c1c0d4b879 | -19.73914 | -41.64688 | 2024-10-02 03:55:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0e5a3df2-e356-3dba-91d3-b275da0da7c2 | -19.73856 | -41.65054 | 2024-10-02 03:55:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 06721671-9358-39f9-8ccc-435fafb59700 | -19.73641 | -41.64263 | 2024-10-02 03:55:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fdb9dfc0-9fb9-37e5-91d1-e129d3d48cd3 | -19.73583 | -41.64629 | 2024-10-02 03:55:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8b27a090-8782-3fae-9987-6aa2fc2aa34f | -19.73525 | -41.64996 | 2024-10-02 03:55:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0e22b1ea-1bf1-35ed-9041-b7b7681b171d | -19.7331 | -41.64206 | 2024-10-02 03:55:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cfd54136-3158-33fd-b616-8d1909508501 | -21.93359 | -41.55497 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 192f2cf0-cf8f-3c17-86cf-a2fb99355bb8 | -21.93233 | -41.77888 | 2024-10-02 03:55:00 | NOAA-20 | SANTA MARIA MADALENA | RIO DE JANEIRO | Brasil | 3304607 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 497bef7d-6016-354f-be86-7bbe9a73085d | -21.93027 | -41.55438 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 11377410-142f-3187-89b3-28984826ca39 | -21.59851 | -41.30562 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4515ca03-8b58-381c-a068-a09619fc9b7f | -21.59794 | -41.30934 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 69fd9e37-1e26-3a5f-b5d0-d6fcec73f5a4 | -21.59565 | -42.12779 | 2024-10-02 03:55:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5603e9b-7992-3f37-a1be-3b8df1acf921 | -21.52131 | -42.06096 | 2024-10-02 03:55:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| de4b3459-63b1-3f9b-b898-9e0257f3578b | -21.51955 | -42.07215 | 2024-10-02 03:55:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 725658e1-e63b-3164-b334-a2972af7b92f | -21.518 | -42.06037 | 2024-10-02 03:55:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aec1b03b-2a19-3384-b970-0d1812a0f572 | -21.48506 | -41.1601 | 2024-10-02 03:55:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51382d83-bdcc-37ba-8341-64970f35adf0 | -21.32454 | -41.41172 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a22d7493-dc05-318a-b2c3-aac694922547 | -21.32396 | -41.41541 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5884b7f5-aeb4-3184-80b5-fc6ae519ee46 | -21.32122 | -41.41113 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a72633a5-41eb-3213-a56a-300561969b43 | -21.32065 | -41.41483 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ef0c7543-66ea-35db-9f8b-6c3e98cfcd5e | -21.31676 | -41.41793 | 2024-10-02 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 47c54b24-8d17-33be-b1aa-156987a3d6b9 | -21.15872 | -41.94783 | 2024-10-02 03:55:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8754974c-3682-3e49-bede-daa0a543fd60 | -20.92268 | -41.83007 | 2024-10-02 03:55:00 | NOAA-20 | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6a7e2907-cc8c-3e51-b801-32e4d2ca29b7 | -14.49871 | -41.55882 | 2024-10-02 03:55:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2bfb3ac5-3d93-3590-8232-0c6d6b957fd5 | -15.8302 | -42.25457 | 2024-10-02 03:55:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb4f3043-a4f2-3dff-a8d8-626239fb9e76 | -17.7852 | -42.89348 | 2024-10-02 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c250d74-f61f-3dc7-a5b2-d07fdebf984d | -17.78172 | -42.80897 | 2024-10-02 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7c67265-8508-3569-85d4-302e37d6ef5b | -17.77831 | -42.80835 | 2024-10-02 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00956a92-b659-33af-a587-9925ee79860c | -17.67682 | -42.74273 | 2024-10-02 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f72aed93-209c-337e-8695-8a9007f4b467 | -17.70981 | -42.37678 | 2024-10-02 03:55:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e723025f-c6a4-3ec3-ad16-a8561c657560 | -17.70644 | -42.37618 | 2024-10-02 03:55:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d94d16c4-e137-3316-8458-86eb798cdc3b | -17.61581 | -42.43444 | 2024-10-02 03:55:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06d3547c-b946-337e-b120-ed89279b0d9b | -17.32511 | -42.36438 | 2024-10-02 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3710d9ef-1bea-3274-bb59-2d56021954ac | -17.87693 | -42.19166 | 2024-10-02 03:55:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d7079373-f2c0-369d-8324-f76975e7784d | -18.9284 | -42.84134 | 2024-10-02 03:55:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f6469efc-3cbb-3d77-8bf4-b1b33ae23e38 | -18.53786 | -42.65531 | 2024-10-02 03:55:00 | NOAA-20 | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8b1497e4-9005-3a8e-a460-179aea02f1cc | -18.34628 | -42.77074 | 2024-10-02 03:55:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e827899f-bd13-3d4d-bacb-91a0fa47f247 | -18.34288 | -42.77013 | 2024-10-02 03:55:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3339ef7-cd56-3d5b-b095-893355da47f3 | -18.34233 | -43.04823 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| df3f1050-eed8-3c4a-bd06-7f5bb9243714 | -18.34209 | -43.04765 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 167c02f9-721c-321b-bb5e-51e7785acce6 | -18.33892 | -43.04757 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 772d7767-7b54-3398-a178-113d9cda1656 | -18.33827 | -43.0515 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| edb81b8a-2490-3cdd-8893-c11b463f03ac | -18.33614 | -43.04306 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2055c324-7917-3027-b808-ba03534bea79 | -18.3355 | -43.04693 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2ab4cbe3-6ca7-3e89-91b8-8de58bf0712d | -18.33485 | -43.0508 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f218629a-fa8a-33f1-a6d3-6e63c91d5d67 | -18.32268 | -43.06037 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9f49d0c4-ef2c-3e0a-ad2e-babb287f976f | -18.19483 | -43.00571 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 57a5c3ce-b60c-3a53-b4af-8fc48a876b4a | -18.11001 | -42.88236 | 2024-10-02 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ecb9ba3a-2dad-3572-ba9e-38d30e171405 | -18.07106 | -42.60896 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8717ceac-3ae3-3da9-8f13-9111a8c68c2d | -18.06768 | -42.60837 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 82a7633d-bcbd-3a15-85d5-16e0f6f21f10 | -18.06706 | -42.61211 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| faa0f53e-9ecd-3fac-83b0-73abf48f2d76 | -18.06643 | -42.61588 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 63952c1b-671d-3b58-aeb1-7b1d01e9c383 | -18.06367 | -42.61153 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f164ef58-4d67-3731-9f53-f8a7cad7b4ac | -18.06305 | -42.61528 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 25b15267-61f8-30ab-b840-ca7d0c8c1516 | -18.06243 | -42.61903 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 261d2ac0-79ec-3eeb-8f7f-737a2b69c200 | -18.05905 | -42.61837 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aeb54691-c97f-3b54-9c75-49f0a5b3a315 | -19.50318 | -42.33201 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| cadeefac-f3bd-30d6-9297-7231e05a0dba | -19.50256 | -42.33582 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 059a2302-d93e-3bc7-b434-43d4c8d9cef5 | -19.50072 | -42.34714 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 776a1539-5221-3cbd-b55d-d94e9189f1b4 | -19.49985 | -42.33133 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac8b3943-cf25-3d8b-a089-51b9ca41f4fa | -19.49923 | -42.33514 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7c6f3f86-1ac2-32c4-b3cf-786608846787 | -19.498 | -42.34275 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ceb7e41a-c6b8-39fb-8326-fdbb4a6cb01a | -19.49738 | -42.34653 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dc41b292-5c74-390b-b65c-b9fd780123bf | -18.78685 | -41.90608 | 2024-10-02 03:55:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cb33ed60-046a-3a7d-88f5-8e84abb7d033 | -18.78412 | -41.90181 | 2024-10-02 03:55:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 49b43177-0811-348a-8164-7b577b15ec92 | -18.78079 | -41.90122 | 2024-10-02 03:55:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8e5b832a-7d9d-3e5f-9837-3cf0d9870fd3 | -18.52589 | -42.23634 | 2024-10-02 03:55:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 825bb392-71a2-3b7d-b74e-afbb08d757e8 | -18.52255 | -42.23571 | 2024-10-02 03:55:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 792c9f93-d178-3af0-b9ef-7e566ccd8927 | -18.52194 | -42.23945 | 2024-10-02 03:55:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 035c7d9b-c882-3be4-9b85-a50304f32925 | -18.5186 | -42.23879 | 2024-10-02 03:55:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 45f62efc-072b-3f74-a00c-e1efcaf9460d | -18.51766 | -42.2235 | 2024-10-02 03:55:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 34b49b53-e3a2-3888-9dd9-17d465b80549 | -18.51707 | -42.22713 | 2024-10-02 03:55:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7f09e9ff-ac7c-3347-b868-783f1f3eae23 | -18.51373 | -42.22651 | 2024-10-02 03:55:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 09db85f9-5431-372d-a5fe-5b4933bc11fd | -18.51038 | -42.2259 | 2024-10-02 03:55:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6cdb4f54-df88-30e2-a039-4425b83f07ad | -20.93144 | -42.93457 | 2024-10-02 03:55:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd9ac625-3d36-383a-bc6e-73fdfcb1a0dc | -20.7624 | -43.59092 | 2024-10-02 03:55:00 | NOAA-20 | ITAVERAVA | MINAS GERAIS | Brasil | 3133907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4d618d44-d2fb-3c42-973b-32c8ceeb444d | -20.41791 | -43.55159 | 2024-10-02 03:55:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ea7c8785-6c75-3d58-9097-2fa385634c8d | -20.41725 | -43.55555 | 2024-10-02 03:55:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3bacf6a9-845d-3ad8-82a4-1491496f2b47 | -20.40912 | -42.90754 | 2024-10-02 03:55:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 298b1e29-51a2-363e-8ce9-96d4afe47d47 | -20.35442 | -42.75699 | 2024-10-02 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 73845fcf-ac6c-3db6-b6d4-0e0f9e6f56e4 | -20.35379 | -42.76077 | 2024-10-02 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 103dd375-bb5e-3a38-9688-23127567b5ae | -20.35317 | -42.76455 | 2024-10-02 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8ac58813-7c22-3c5a-b719-656ade244328 | -20.35107 | -42.75637 | 2024-10-02 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5845cc16-85f6-37c7-bd2a-acae9d9f58fc | -20.35044 | -42.76016 | 2024-10-02 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3b08cc36-88b8-3975-b6a7-eed5c6253952 | -20.34982 | -42.76394 | 2024-10-02 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 011736bf-dbb1-3c59-a6e7-03b1c957d735 | -20.30119 | -43.13912 | 2024-10-02 03:55:00 | NOAA-20 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5dc0e95e-3b60-356c-9294-5e21436331a3 | -20.29845 | -43.13463 | 2024-10-02 03:55:00 | NOAA-20 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0a23bc97-d575-3784-89ba-31f234f4dc44 | -20.8175 | -42.29736 | 2024-10-02 03:55:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 175892e1-a844-309d-889a-7f0a41860dbf | -20.8169 | -42.30108 | 2024-10-02 03:55:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0adef047-678e-37bd-bbd9-46f5749607a3 | -20.8149 | -42.18599 | 2024-10-02 03:55:00 | NOAA-20 | PEDRA DOURADA | MINAS GERAIS | Brasil | 3149002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README69.md)
