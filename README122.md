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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40322441-08cb-37fd-879b-02d3bbb68532 | 0.29786 | -51.08803 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f59eca60-bcd5-333e-aabc-6bfa77b35ee2 | -2.87366 | -54.11391 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2de10b6-f4ab-350d-834a-544fe1b9cbb0 | -2.5439 | -65.87098 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 48bb9418-a79b-387b-a4e2-68cd3009d604 | -2.76095 | -57.65003 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5b21bce4-d39d-347e-b31b-e907a2aab4b1 | -3.28776 | -60.11367 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 36b8ec9e-3355-35ce-9807-26ed2e2567f2 | 1.87139 | -55.76788 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30609784-cc78-3fc3-8f6a-4db58cd59bc6 | 1.73128 | -55.62302 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 618f2904-c326-3c49-8b0c-421452514dfc | -3.67503 | -60.53843 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 87b81b0e-5a4a-3ebd-a8db-79f421fa94bc | -3.1218 | -59.26311 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9718fcaa-4404-3e47-aba7-f3dbbdface76 | -1.46008 | -53.61165 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 636d59a4-b600-30e4-a8a0-f52049e384dc | -2.98386 | -57.8983 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dcf806f7-c9fb-38f1-b724-0f36b4169d74 | -2.98756 | -57.89774 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5a1ab201-91bc-3a80-b3d5-81d973f443aa | -3.28716 | -60.10971 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c8c868fb-29f4-30f7-ba07-cac2177791b8 | -2.09759 | -54.61066 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3eb4367-5bb6-3d3e-b278-13ffc68bd5f4 | -1.90026 | -56.61036 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 990bb32e-a58b-341f-bbd6-522a481c3e42 | -2.97583 | -54.07638 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5392f4c6-1598-311c-8e4f-7c78b5c18e7c | -2.63685 | -56.66105 | 2026-10-05 17:17:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f2e07f6-ecfa-35f8-aa62-509a173b84f9 | -2.95533 | -54.16421 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e0cd4a53-41ce-38ba-a6a3-a0195bdfa74a | -1.95003 | -54.04393 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd1f14d9-50f1-3c99-a8ae-6c4b0080379c | -3.22228 | -64.80744 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e1be9359-112d-3da8-b0b9-072cfae42d9d | -1.44251 | -55.23618 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| acf1751c-3ca0-34e6-a587-8f694fe77228 | -1.46399 | -53.61467 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fb16392-bcda-37d9-87c2-fda3a4b12687 | -1.89778 | -62.46894 | 2026-10-05 17:17:00 | NPP-375 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22e8cac8-2394-3183-83c4-44bc9f3e8f00 | -2.9548 | -54.16076 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| befd7ddc-ef09-3503-b609-82075f73d775 | -2.90158 | -54.07441 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9a903e3c-56d4-317d-8a1d-93547f0432af | 1.90999 | -55.71453 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cdcf2850-cc46-3b00-a4a3-2bac1ad28be8 | -1.4629 | -53.60762 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7eb8a29b-e19b-3379-b24e-49bfd552b4d0 | -1.61859 | -55.10617 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7dd96d4a-5aab-3b86-860a-61ac7b16f2d8 | -2.0938 | -56.62296 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c46341e8-5e86-33f5-84f7-b6797e0cf7c3 | -1.81807 | -57.10414 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6c27454e-437b-35e8-8c51-98dd871ff337 | -1.12234 | -54.117 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 82a32a26-c702-3b3d-9970-9eed793a906d | 2.257 | -50.82106 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4e225880-7a8a-3167-a24c-a5f8337bde39 | 0.30773 | -50.99884 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 61039077-fce1-3b20-be32-a56b874a6424 | -1.73514 | -56.0753 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 303b5e37-8ffe-36e8-9b57-66c825aa84a4 | -2.33906 | -57.98547 | 2026-10-05 17:17:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2188c140-2afc-3b55-a88c-279669d99510 | -3.62051 | -64.34509 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ec096a52-da14-3419-84c5-bffec91665dc | 1.57553 | -55.99773 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38520434-6fb4-38a9-8058-99569d857f66 | -3.75186 | -61.01826 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 82ecede6-14cd-3a58-aff8-697ee7cda102 | -2.94724 | -54.13365 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51254e5c-18fb-332e-94ac-5305754da6a0 | -3.50212 | -59.55995 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4c4b21d1-2ebf-35db-93b5-c65ce5af350d | -0.83359 | -49.29001 | 2026-10-05 17:17:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 59a01ca7-9c58-3283-81f6-d01885017cb6 | 2.11912 | -50.7645 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c02c7b5-4971-345c-bdef-6365bdc3c06c | -1.46126 | -53.59704 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f495207c-cd1a-3ee2-bc0a-dcfc5587d5f3 | -2.95681 | -54.10746 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 839843a3-8529-33c8-972f-d95943db5e5a | -3.65389 | -59.1609 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d91c7b1b-9914-3a37-a084-aa95e1d8431b | -2.54206 | -65.87479 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| b549e8b8-01f8-3852-b8ed-8d31ca49f346 | -4.09203 | -63.04793 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea8394fc-336b-36cb-b82f-7e1a3eae0319 | -3.75573 | -61.01299 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 43155680-100b-3983-9717-73c8959b3362 | -1.30785 | -54.22291 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b97eb500-decf-339d-9b9e-05187095e9e4 | -3.64769 | -60.91947 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 2f1d3bb3-0184-321c-975f-776f76c03fa6 | -2.87313 | -54.11045 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57ccd541-3e8f-3f4a-b423-57053bd6ea7a | -3.33158 | -59.47724 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 74e7597f-1392-3399-b438-77cec1c64e57 | -4.27019 | -63.66373 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3efc2e94-e8e9-3d92-baa7-cc9008799059 | -1.37382 | -55.99985 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d17609e2-4479-39d1-8af2-39d4f5ca5c72 | -3.36903 | -58.18586 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d1c0ae27-0c87-3c45-b827-b1c718f1a8b0 | -1.31118 | -54.2224 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 41d1a330-860a-3151-9b48-41e227ebc5de | 1.87297 | -55.75754 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0462c32-05a8-385f-97eb-675494472b11 | -2.97304 | -54.08033 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71bd0f0b-b78a-3a97-8bf6-8f91d2d70902 | -3.33211 | -59.48086 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d2326413-2dd9-36eb-a2de-2e4e9f7c832f | -1.13256 | -52.02006 | 2026-10-05 17:17:00 | NPP-375 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dfc9f4c3-dbda-3e22-b49e-72d13a31ad9e | -3.51449 | -59.55814 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 15ee7087-9253-3cc0-b7ec-567e4286f316 | -1.62201 | -55.01735 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90bbae68-8be3-3d15-9855-bb6b04f8dddf | -3.64008 | -60.92213 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| eb899300-8840-32e4-afdc-ed13b5da20ea | -2.04678 | -54.30099 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 97ff366f-34e2-3fc6-9fa5-b14894adcaf6 | -2.89849 | -54.12075 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e7ebfbd4-6e48-3bff-8559-8798b9d99833 | -1.19471 | -49.25827 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 8051af7e-1c14-3955-8e78-09d4a637cc90 | -3.17302 | -60.06479 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| cd02c9f4-a765-3587-9e53-310cd4db82f0 | -2.86355 | -54.13664 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e7a124c-a5ef-3d79-b9f2-383baa33c945 | 3.51729 | -51.5001 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2fd7165a-5f5a-345b-9fc2-ab75251fc755 | -2.92981 | -54.14779 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b425b1af-be45-32b5-8bcd-a882e24e1e2b | 1.59843 | -51.00257 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6222ced6-3642-3f41-bdd0-55ab8f6f5438 | -2.96645 | -65.19314 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 25ec6937-908e-3c73-bc9f-931b14a5494c | 1.86317 | -55.77721 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce6835e6-a11e-3b3c-92fe-0a91b0c9fa89 | -1.46235 | -53.6041 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f4344f39-f263-3ac8-8be1-b89afaa26eab | -2.54866 | -65.86049 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f783a15e-ea04-3da9-aef7-f7cb54ce6ef7 | -3.77537 | -61.18531 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 19318f95-a8f2-3c15-835a-f6642c5efc5e | 1.45824 | -55.66043 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 01cd0d29-4f52-3ca7-a17d-a6cfd125211f | -2.95932 | -54.14595 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| acb1d973-4007-354c-89a6-ac114bdc509f | -2.91155 | -59.298 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a188500e-41b1-3fbe-8a07-4d95bba00e93 | 1.97922 | -60.61508 | 2026-10-05 17:17:00 | NPP-375 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 81e334ae-5918-30fe-83ca-5c9ab7254689 | -1.6158 | -55.11013 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3e6095b1-b9a6-39a2-b903-fe91c7d6deb4 | -1.61632 | -55.11359 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 02434011-817f-33bd-b701-ba2c72971146 | -3.51037 | -59.55874 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 39bb238e-3da7-30a7-91b4-ef8309f84157 | 1.73896 | -55.61714 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a0a9a1da-e418-3bb1-adc6-2861c393fb59 | -1.70597 | -51.99573 | 2026-10-05 17:17:00 | NPP-375 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 8cbce013-b26e-3e09-bb19-9701ad5841cd | -2.7842 | -57.68089 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d936b60a-24ad-32f7-ad16-ab3fba39692c | -1.45777 | -55.26929 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ca3e1a99-f6d5-3eee-8479-f10000685b63 | -3.82466 | -61.13459 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| cc3dfabb-783e-32b4-8a61-a9719913ac83 | -2.98723 | -54.10638 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3137ef3-b96a-379b-b526-d8f870bdaf29 | -3.17971 | -60.0518 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3996b18e-6e33-3cd0-9262-e1022c22ba11 | -3.6745 | -64.22993 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dcd241fd-332b-3084-8328-565a6a3653bc | 1.61503 | -55.78449 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ab45dc0d-c9e1-34a6-b5a2-38ac4b0ab212 | -2.86056 | -53.91778 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6614675f-3bb0-3ab9-8a0a-fc26f812f4f3 | -3.62969 | -60.20821 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 881a00d7-d594-32b5-bef8-19121abc4ca8 | -1.32177 | -53.14968 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c10d184f-c47d-3bb4-b310-340e07ce9b39 | -1.7804 | -53.77458 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad4b945f-c457-3c9e-b6b1-346c03cca23f | 3.49358 | -51.44373 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 360ec03f-aaf5-3f83-a7ac-6f3ac46e475c | -1.7007 | -54.93415 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46f17936-0744-32e2-8624-3b4c8d6ecd59 | -0.40556 | -51.999 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cf16aef5-20d5-30ae-8eff-3abc953844d2 | -1.52479 | -54.82135 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README123.md)
