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
| 509119a3-d7a4-3c37-b6c4-38ea5c292597 | -15.3682 | -58.153198 | 2024-09-30 01:11:26 | METOP-B | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc14bf62-5d00-365d-af05-41890c69e3b8 | -15.3698 | -58.1609 | 2024-09-30 01:11:26 | METOP-B | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4483028-15df-348f-9a78-a755b672369f | -15.2784 | -58.165199 | 2024-09-30 01:11:27 | METOP-B | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da1d5b95-804d-377a-8c3d-d6e5f8d180e9 | -15.28 | -58.172901 | 2024-09-30 01:11:27 | METOP-B | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68c6eb81-ae4e-3617-95c2-fb350cdded52 | -14.9331 | -57.939999 | 2024-09-30 01:11:32 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91907a50-1239-3661-8060-a26388e7359a | -14.9037 | -57.946602 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95792de7-3ad8-361b-974c-097f10a449ec | -14.9053 | -57.954102 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f507ed6-8720-344d-b18c-56ed1dafe20b | -14.9069 | -57.961601 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc3fca4-4774-32d2-9219-28caf8049283 | -14.8889 | -57.9734 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab454807-6d99-3243-8c07-30b0e307ca87 | -14.8906 | -57.980999 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38f310dd-cae3-3fd4-90cf-0ee3d3fb2632 | -14.8922 | -57.988499 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30de5184-388c-383e-99b1-331d35f28da3 | -14.8938 | -57.995998 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3845c2c-cd4f-3328-a34c-a49539c4344e | -14.8808 | -57.9832 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1ce44e9-fa15-3d61-8c71-2b381c26c7b8 | -14.8824 | -57.9907 | 2024-09-30 01:11:33 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1ca5c53-4511-31bf-9b0b-f0f570847004 | -14.7724 | -58.197601 | 2024-09-30 01:11:36 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f99e772-ac9f-3788-b202-80bc26c990d4 | -14.7741 | -58.2052 | 2024-09-30 01:11:36 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b451aec-593b-3651-816d-f6f99ebe0495 | -14.7757 | -58.212799 | 2024-09-30 01:11:36 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0916677d-8a79-34ee-98ab-d46ce4b02985 | -14.7643 | -58.207401 | 2024-09-30 01:11:36 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8b455532-34b4-3677-b9e1-8e362bf9fa2a | -14.7659 | -58.215 | 2024-09-30 01:11:36 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76335bc5-2002-342e-b33f-800748910091 | -11.9689 | -47.265999 | 2024-09-30 01:11:39 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0098e85b-4f01-39ae-9e7c-036753b02b85 | -11.9743 | -47.2869 | 2024-09-30 01:11:39 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1548c6b-cbac-393b-8d62-4f816e3db9ca | -11.9647 | -47.289501 | 2024-09-30 01:11:39 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de035ca5-be7f-387b-acbd-879a3cd02ce1 | -11.7826 | -47.580101 | 2024-09-30 01:11:43 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3587282-32a4-3259-9bca-e6337cf82a07 | -11.773 | -47.582699 | 2024-09-30 01:11:43 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09e3baca-9d7a-3ed5-9e60-9afbbf6926ff | -12.5245 | -50.628899 | 2024-09-30 01:11:44 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 575f08ee-6d60-3a64-a1ef-34b3cf80dfce | -11.1647 | -45.626598 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49a12138-f945-3d27-9002-fa6ddddb459f | -11.1721 | -45.6544 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ade35caf-1b07-3a2e-818e-4712a7fb14f3 | -11.1795 | -45.681999 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff0ae0b-ef14-3161-9ec5-15d8d433fd7d | -11.1401 | -45.5732 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3b4203-32e4-32e3-9cf2-1549c85e9f86 | -11.1476 | -45.6012 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e755f849-3623-325c-9d35-c9728eb4b3dd | -11.1551 | -45.6292 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f972ea99-c8aa-301a-8c33-7e10cc28e482 | -11.1625 | -45.657001 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c28da63b-59a7-3eb1-974e-ca639dacb932 | -11.1699 | -45.684601 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25dc6b87-9353-3b11-a132-a82ffbdc970f | -11.1772 | -45.7122 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38ce2f61-b6e4-3493-a38e-f4856037bae9 | -11.1381 | -45.603901 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09667253-8c8f-32a8-ab2d-81cfb7d46291 | -11.1456 | -45.631901 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c8a382f-44a1-3e77-aef4-eb2841d93834 | -11.153 | -45.659698 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1eb312-cdb9-3d4b-9281-df26710d26c8 | -11.1604 | -45.687302 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb43b54a-596a-3c03-b3c3-a9de151c5cb8 | -11.136 | -45.634499 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2c5a35b-c944-3ee7-b317-e126d6782cd5 | -11.1434 | -45.6623 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67f1c7f8-39a3-3190-ab1f-38cafd097e0e | -11.1508 | -45.689899 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8dbebfa1-89af-34ed-9a63-fbc0b1f8b015 | -11.1581 | -45.717499 | 2024-09-30 01:11:45 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8031aa-4159-3379-a47d-bc5ab61aa6be | -11.1264 | -45.637199 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2368b206-4955-3070-a8a1-365348a14cfd | -11.1338 | -45.664902 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f2f6bbb-a8ca-399b-936f-5bf25dc59879 | -11.1412 | -45.6926 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a4d5cdc-d28e-3274-832d-aacdc258b6cf | -11.1485 | -45.7202 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10a8bac3-cd89-33ef-a150-934d800fd8fd | -11.1242 | -45.6675 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9efa128-9760-3724-b523-68a67134c7ba | -11.1316 | -45.695202 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21f188b0-6e60-3f32-87e3-4034f35bd65d | -11.1389 | -45.722801 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b8c1f65-1cc2-30c8-8890-f3f96c1b9312 | -11.1221 | -45.697899 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c98a2c0-9498-324e-95dd-80f936bab1a6 | -11.1294 | -45.725498 | 2024-09-30 01:11:46 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65f56a96-0299-3d85-ab41-27af85793fcc | -11.1319 | -45.928001 | 2024-09-30 01:11:47 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21723511-3338-3c9f-b994-062944898e0f | -11.139 | -45.954601 | 2024-09-30 01:11:47 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 316ff95b-006b-3621-b612-1b6ed0118aad | -12.4176 | -50.949699 | 2024-09-30 01:11:47 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b894cd3-4e51-367e-9a13-c2b68b914cf4 | -12.4204 | -50.961498 | 2024-09-30 01:11:47 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04438533-9f19-3f01-ae27-5a5127297955 | -11.3933 | -47.193699 | 2024-09-30 01:11:48 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a279c0d9-4bd3-392d-a40c-49a16a1e3512 | -11.399 | -47.215302 | 2024-09-30 01:11:48 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4657f09-24d3-3992-8bc4-27dad8d90935 | -11.3837 | -47.196301 | 2024-09-30 01:11:48 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c403038-b8a6-358e-9951-8954c9f9621d | -11.3893 | -47.217899 | 2024-09-30 01:11:48 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a0030d6-ed0a-39e2-9e6c-79d717d36088 | -11.3797 | -47.220501 | 2024-09-30 01:11:48 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c4d5cae-762e-3b50-8b87-194ea83d5669 | -12.0788 | -49.999298 | 2024-09-30 01:11:48 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8428d672-7b86-39dd-9690-5ae22cb74fd9 | -10.8934 | -45.457802 | 2024-09-30 01:11:49 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2795dd68-9dad-3cce-844e-83041a95edf9 | -12.2177 | -50.641899 | 2024-09-30 01:11:49 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0049096c-d4a4-367e-a8ef-7b6cce489756 | -12.2207 | -50.654301 | 2024-09-30 01:11:49 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff1443f5-fbb9-3d90-a3b2-751f66eb1128 | -10.9628 | -46.416 | 2024-09-30 01:11:52 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e18b8b95-ad08-35c6-a01b-3d09a2399e20 | -10.9694 | -46.4408 | 2024-09-30 01:11:52 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c4364e3-e009-3827-8744-fff90798e911 | -10.9532 | -46.418598 | 2024-09-30 01:11:52 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b1b390f-544e-30b7-8739-feda7c5dd186 | -10.9598 | -46.443401 | 2024-09-30 01:11:52 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a672eab-e3b1-3260-be13-6dfd8016d7df | -10.9436 | -46.4212 | 2024-09-30 01:11:52 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66552c3e-8637-3e65-bedd-5dae5e2548bd | -10.9502 | -46.445999 | 2024-09-30 01:11:52 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bacc8f8-7ce2-3b1c-ac0d-b246c212cf18 | -10.9406 | -46.448601 | 2024-09-30 01:11:52 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a6f49a2-9ce2-3700-a603-5d57029f5187 | -12.7907 | -53.976002 | 2024-09-30 01:11:52 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0ea5f0-980d-3cf9-a00b-5eba63e75213 | -12.7925 | -53.984001 | 2024-09-30 01:11:52 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6e6471-676e-3feb-a833-82ce790e7c04 | -12.7809 | -53.978298 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33355f67-5feb-3421-b352-9f400d4b78b0 | -12.7828 | -53.986301 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad4ae7ce-5773-305b-a115-d8de8ee5bb9d | -12.7692 | -53.972698 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 065423cd-bd96-37b1-a4dc-2596e3a58ea3 | -12.7711 | -53.980701 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 373daf09-3d1d-3155-9af2-fe62746a468e | -12.773 | -53.988701 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5ab7786-2846-3a74-9c8d-f8a6043a965e | -12.7594 | -53.975101 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90b82e8a-84b5-3648-abb6-c84d5fae1e8f | -12.7613 | -53.983101 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e7ac88c-d790-333b-95c9-7d5563eadfba | -12.7632 | -53.9911 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44c76788-ff0f-3862-8288-6bf6c43aebb4 | -12.765 | -53.999001 | 2024-09-30 01:11:53 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1576779e-ddbe-34f4-a4ae-17ee12b8e51c | -10.6793 | -45.8494 | 2024-09-30 01:11:54 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0909271d-e95b-3243-94af-9e8bdfd94df0 | -10.6865 | -45.876801 | 2024-09-30 01:11:54 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7249c87-913b-399e-b18c-f953d902d3f7 | -10.6697 | -45.8521 | 2024-09-30 01:11:54 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f48c2cf0-0401-3d31-aa81-59be57a2f438 | -10.6769 | -45.879398 | 2024-09-30 01:11:54 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e359ecdb-737f-35ca-a83d-eff634c71a02 | -12.7241 | -54.0005 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3a2a1b-1468-3c6c-b2c7-c7951a20dd62 | -12.726 | -54.0084 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76971bfa-13c3-3d21-a34d-7573fdae10ff | -12.5104 | -53.134701 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec6ba4c-d1c0-3176-b11d-07b048edcf1e | -12.5125 | -53.143501 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d83933b-48fd-3f68-a56b-a5a95ca589b6 | -12.5028 | -53.145901 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6364b0ba-3863-38bd-81e0-2d558e44859e | -12.5049 | -53.154598 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 578ee812-4972-3c7b-8363-ccbd3c508127 | -12.5069 | -53.163399 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c063cb1-19eb-3a23-b71c-58a324e0a96c | -12.723 | -54.084599 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 554ddbf0-2003-32b1-a44b-b1e7468e898a | -12.7248 | -54.092499 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69f56d69-3356-3764-b081-b0bfd6602e95 | -12.4971 | -53.165798 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a41957d-100f-3aa8-b150-c991ba4975c5 | -12.4992 | -53.1745 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b68bdee5-6686-32ff-83be-1a1f0afa07fb | -12.572 | -53.483299 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95108c7d-13bb-33ab-9d98-c84d833ba5c4 | -12.574 | -53.491699 | 2024-09-30 01:11:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54546b9c-a01f-3496-8c80-0c1e453d1a73 | -12.7114 | -54.078999 | 2024-09-30 01:11:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
