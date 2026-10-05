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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 343af3a3-3fb3-33be-ae21-116dc3d9d845 | 1.30267 | -51.12743 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 329a28d9-06c6-3e91-8a43-42517c71ab31 | -3.06692 | -58.40818 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6b92ebce-7432-3b3a-a675-0779afb2910c | -1.61247 | -55.11063 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 022fa958-976a-331c-9ec8-a2611b10b695 | -2.09097 | -48.83863 | 2026-10-05 17:17:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 43327d75-d5a0-3e03-9532-c8aad85cad97 | -3.32236 | -59.47125 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9b0d6aa3-6130-3f0d-b96e-9e5c88da64c1 | -3.4885 | -59.72523 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 14dd0bec-8dea-3732-9aaa-28c0700f29bb | -2.38406 | -56.12317 | 2026-10-05 17:17:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0efded40-c93c-34ec-8a31-ef402405084a | -2.88113 | -54.07398 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2933effb-1cbc-3651-8431-834d9290f61c | 1.98383 | -60.61216 | 2026-10-05 17:17:00 | NPP-375 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 6a6429d2-d109-3bc5-ad75-54231998db71 | 0.44401 | -60.53347 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 009dcfb8-242d-3a2f-a261-68923742b632 | -3.7242 | -59.40822 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5e9f88d0-a7eb-3318-9e31-76ead7c6a77c | 1.86159 | -55.78755 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f476162-ec12-37ea-ad5e-3b3af3a82f8b | -2.86913 | -54.12873 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a77a1e0e-f75c-3a57-8431-1c0e7ed73b19 | 1.29627 | -51.12944 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 30bf5b0c-22f3-37ed-b0cc-8c5f4ca0dee1 | -2.92701 | -54.15174 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eadeddfe-8171-3be5-bfe5-593fb261ec09 | -1.19052 | -49.25893 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| b2ce06e8-6966-33dc-a070-4c35349bff65 | -3.5332 | -58.67266 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 782e75b2-2a59-33ae-8caa-2c14c7d8f280 | -2.94764 | -54.15831 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0508809a-ee06-35d2-8e6c-227b00661658 | 2.27631 | -59.78938 | 2026-10-05 17:17:00 | NPP-375 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da12acde-2d98-3dca-88c5-3ff94f7d51ec | 2.39785 | -50.89688 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 56a92d9e-4f51-3fa4-ab49-c476dfaf0979 | -1.10648 | -46.64615 | 2026-10-05 17:17:00 | NPP-375 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 61aba69c-13a6-300b-9b6b-0d6a0e27fce9 | 3.53281 | -51.50237 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73e37f1a-a80e-3868-bf76-880f49b9309c | -3.6801 | -60.54208 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 73ba0000-2558-32b7-a262-83a63e2663a6 | -2.9694 | -65.19611 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ca917acf-d67b-3f1f-902e-0ba0d9caa634 | -2.01699 | -66.32381 | 2026-10-05 17:17:00 | NPP-375 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 378659ca-28ee-313a-8fde-3a4a4c6c0f8a | -2.90649 | -54.08427 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 55f7a16b-bae7-37e8-81dc-2915ef68a52b | -1.28115 | -55.41801 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49549325-52ef-367c-b02d-d22be8ccd23c | 1.74001 | -55.61026 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f1af33d-79da-3ef7-a2a5-1a7421af4c7d | -2.80236 | -54.09016 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bb871c2d-9969-32f2-bde0-c30814898d59 | -1.66423 | -49.64055 | 2026-10-05 17:17:00 | NPP-375 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d4acfbbd-a927-3c09-99a9-c800301505c1 | -2.70512 | -57.15822 | 2026-10-05 17:17:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 87348fd2-4510-3d23-a180-eeeb4926de53 | -3.62448 | -58.61662 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1a665942-b10e-3fde-84f8-6da4cdcc60c1 | 3.41915 | -51.51707 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 61d75fa3-4c3b-395e-b2df-d6ef8fe5d62d | 1.60402 | -55.78987 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3eae8586-468b-3cc4-919a-bc48d86fbb30 | -1.74714 | -55.23824 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97d9e556-5c52-3920-8dad-e0e67be3b486 | 1.79748 | -55.54506 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 33953cc9-5274-39c1-8a03-69de54871cd9 | -4.28512 | -63.41636 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a37ff449-e457-3070-9524-75312b0754a5 | 1.88223 | -55.74132 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c7980c3-290d-330a-af6f-f3af5fd809e5 | -1.1904 | -54.13869 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c3de5ec6-346a-352d-984a-8028e2efe2f9 | -3.28627 | -59.41856 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6cd4ad00-321f-3da3-b23d-7c6d72420447 | -2.07678 | -56.83765 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2580e2d1-caf3-3ee1-9e3f-10168c4556c7 | -2.98081 | -57.90318 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 34800e4e-3a3c-38d1-8cbc-acab06328ca4 | -3.54416 | -59.48684 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| ccddff08-f8d1-35f1-a5e5-5936da7436a4 | -0.71574 | -57.96585 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a614cb8e-67f0-3aee-a136-df78d8ff3c85 | -1.46057 | -55.26532 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 7f3dbbc9-1470-32a8-9a2a-7e614c17a8bf | -0.37743 | -52.07809 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 824aaa74-b548-3f76-8b5d-de6443424314 | -2.96711 | -65.19753 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 43201a7b-7bd6-3fd6-ba1a-27e1d882ae14 | -2.54535 | -65.88059 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e7d3b421-f115-3b95-82de-8550634b6199 | 2.09144 | -50.90777 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3f84449-2e64-3e8e-9a17-cb8e34342547 | 1.85337 | -55.79689 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 16712bc9-c415-3252-8e7c-c3a83e3522e3 | -2.87524 | -54.12427 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 79d14a6b-1da5-3dde-9088-d608e948d3d7 | -3.67991 | -58.88618 | 2026-10-05 17:17:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| be415a28-8531-35fd-b5b8-9f852577fe8c | -3.46781 | -60.26033 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55117caf-6f2e-3c45-8acb-06d2c18eef39 | 2.40182 | -50.89747 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6a6b2df7-05cf-3366-9016-c717bc092d1c | -1.63417 | -56.00704 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0ce14da-8bc9-3ef3-8fa1-fb99dced237c | -3.48488 | -59.7296 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a5a602f2-0d53-3d9e-8a05-e7fb3907788f | 3.35232 | -51.34592 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6711343-1a58-38f0-b864-4419471f2ffa | -3.37646 | -58.23598 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a169fe9e-ef4b-3b71-949a-023685ef8928 | -3.7487 | -59.62648 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e586d051-f5a3-38bf-ae4d-bf021ddb3bd8 | -1.33136 | -55.28221 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7486c4bf-ec36-3824-b96e-c3d42588d1ae | -2.03735 | -54.30595 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c76102a2-b082-3796-8636-ed1f93f92816 | -2.78244 | -54.09318 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 69e6220a-e6a6-3386-9f75-35cb296d34bd | -2.55167 | -57.98751 | 2026-10-05 17:17:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2ebfc94e-3025-38ab-a60a-35d259e66193 | -1.20186 | -55.69461 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bbdddbca-64d4-3321-a8a1-33947c0bbab0 | -3.50982 | -59.55508 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8e0de199-a9a8-393c-90f6-9c91a26de66d | -3.23839 | -64.83504 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e34ad02d-0b8f-33de-8ac8-b99ecdbb1a41 | -2.04625 | -54.29754 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3adec580-48ca-3fbd-b46a-4bb603d71385 | -1.57115 | -55.30181 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f13735a5-d1cc-3ca5-bce8-3593598bb8a6 | 3.35696 | -51.34159 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 77b350be-fef1-3845-88b8-86e417d41f51 | -1.63456 | -55.53777 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2693a94c-7c31-3beb-8915-e2acd0f7a2d4 | -2.7924 | -54.09167 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 80b9ed71-c7c8-3484-8b17-875c2b0ece55 | -3.42105 | -58.56391 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3689b236-8137-3767-8112-d853cafb51b4 | -3.54592 | -60.51694 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f415eb8b-53a4-3f9b-ba21-6d11fffa64d3 | -1.91317 | -65.46332 | 2026-10-05 17:17:00 | NPP-375 | MARAÃ | AMAZONAS | Brasil | 1302801 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b251bf52-7e29-3177-a7b7-a2527bafdf05 | -1.20466 | -55.69061 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 14bba7af-d6eb-3064-a081-5e193a791aee | -2.03003 | -54.32471 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35f900fa-fa8b-3c12-9408-1478d1d6e931 | 0.80509 | -51.14643 | 2026-10-05 17:17:00 | NPP-375 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0eaf124b-edb4-3815-8286-8add4e9596e6 | -1.51511 | -55.95918 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2be75e1e-43a5-31f0-bbc6-f2a650509bbd | -2.95148 | -54.16126 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f6b0de1f-d81d-3ac8-bd2b-1aa7b5b937af | -1.69675 | -55.01944 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 349aa3f6-2957-3648-b034-3517be9f85f8 | 1.84131 | -55.80917 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 13d3a0ee-cb0f-3c5c-94b0-0aeb85f79e49 | 1.7926 | -50.6227 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 617c9925-2384-330d-aa4b-9220f752616a | -3.74017 | -59.41275 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e6f8bd3-ce01-3111-a076-8898d20c9188 | -2.9701 | -54.10544 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c03902ab-69db-3402-936e-c2d5e9653966 | 1.85933 | -55.78016 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2df35fa-85c1-35ba-b84d-d782a4032ca4 | -1.19821 | -54.21202 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 166ab688-3c2f-39f5-a0c9-39124a57d666 | -2.9452 | -54.15958 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| e8ccab47-e2a9-318e-9984-e5c6b91e6b6a | 3.52434 | -51.50607 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ba4843c0-dbf0-33e3-a129-34cf6bc057a0 | 1.97866 | -60.61866 | 2026-10-05 17:17:00 | NPP-375 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7235af3e-1951-3188-8d2f-08289fc166cf | 0.05862 | -60.42894 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2cf833e2-d661-3bd0-9b30-fb27802c5f2d | -2.2713 | -55.8391 | 2026-10-05 17:17:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 916f66cf-d120-3773-938c-8b6ae02049a1 | 1.89057 | -50.66195 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef72a090-9f1a-3437-bfdd-10cb582f7232 | -2.90211 | -54.07787 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 94c78b3f-a845-30b1-87d4-5dacb21ba353 | -1.94106 | -54.71351 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4734d69a-a992-3cac-8ed3-1c3432a5f15e | -1.21417 | -54.53826 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2b1cb3eb-7ea5-389a-bb6f-40f7167b752c | -3.28681 | -64.9362 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9bd9343f-0f92-3d89-933c-5ccf47dd0a56 | 1.48773 | -55.64452 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 016693d8-2256-3977-8d1a-5f598be5d740 | -3.37267 | -58.23654 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 881f8d74-c05e-3730-96f0-c94a7052171c | -2.04731 | -54.30444 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac69bd1f-9bf9-3ae4-95c1-edd9d727edb5 | 2.49216 | -50.93417 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 37.7 |


[Clique aqui para ver as próximas entradas](README129.md)
