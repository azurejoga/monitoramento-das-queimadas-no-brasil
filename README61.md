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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 613d8bfe-80ad-371d-a0ad-bb16d52a63ff | -10.65812 | -50.48242 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 113360c5-271c-33ea-a38c-c48d3eb852eb | -10.4074 | -48.6793 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c9cd760-ad7a-368f-8c69-48ddc6a636a6 | -10.61559 | -46.07641 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f435fb54-2095-3760-8b19-94e8b59d1130 | -12.6243 | -50.89298 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9b02a14-137a-3fe6-83a3-d65cb4afb90e | -7.67103 | -46.08292 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fc5dc6b-23aa-3fb5-8d59-5f5ea0c9b251 | -7.01821 | -44.6596 | 2026-09-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06025b27-5100-36e3-8e8b-9f9cece331ba | -10.99823 | -57.06416 | 2026-09-18 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efb36b58-25c2-3b70-b179-a948f0d24112 | -9.77134 | -46.59227 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ea49d8b-0774-38cd-8a96-ae86e81482f9 | -12.34886 | -50.77831 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81635c36-f06d-3f33-90a6-6f5eda933e07 | -7.00239 | -43.63967 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a08a53cb-930c-320d-a68f-faf11bdf37ce | -7.02383 | -43.627 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93243f32-080e-313a-a071-44eb79463d38 | -12.16751 | -46.99478 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8322ca5-bfea-3fa6-abe4-5ec8ed196418 | -8.70132 | -44.8895 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d248ff6-c86d-31b3-9d33-38144cbc57e7 | -10.89041 | -53.99777 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b0197f5-ef1f-3a25-aeee-76d68ac022a1 | -9.69285 | -54.3344 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f8f4305-dc72-333f-ab16-4cb7c4f239aa | -12.51842 | -47.0913 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dc4f2223-080c-3ce4-9e10-8f5d362c75d7 | -7.82291 | -44.90399 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e44a320e-07ec-3993-acd8-3cddca86fffe | -10.66211 | -50.27454 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7af7007d-7b8d-354a-9a28-fd823de75411 | -8.85539 | -46.92868 | 2026-09-18 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e97502b8-5da6-3db3-82ac-b8a30c116f6c | -7.04644 | -42.07738 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 64881e68-f90d-346e-9c13-f6aabc903413 | -8.88128 | -45.89183 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 333c59e5-cf0b-3ede-9f3b-090574f67399 | -6.67061 | -50.90051 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6e79bc-72c3-3e45-a269-387ed75dbf4c | -5.88633 | -52.09085 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a26ad39c-fd6c-3bf6-8c42-69fb49642e2e | -7.67813 | -46.09154 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 502faa03-a877-3c58-a3be-f28056839b82 | -9.24228 | -46.19418 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1ded004-4029-3de6-8d9f-78e5ea835f68 | -12.39654 | -50.69409 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea07fbc0-96b1-318b-80e5-7ddee5b3e3c2 | -12.38527 | -48.47384 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8d54efa-80cc-389f-8566-94d810815dcf | -12.41592 | -50.70482 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00582118-a55e-39ae-a69b-610e722e467a | -9.70512 | -54.82142 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 06c46fa9-08ec-3cb1-9a63-88f286302a1c | -9.63289 | -47.80688 | 2026-09-18 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40600a0c-9e39-30b0-839f-a8bf867d71f0 | -6.65456 | -50.91576 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a371aaf-8406-3a47-99b7-9b906f55e14a | -9.57534 | -49.11086 | 2026-09-18 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afd02883-62a4-349d-8547-bc765724af8b | -9.5598 | -45.47702 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74add84b-262b-3b54-b2b5-1632406dd6b2 | -10.63019 | -46.06583 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0344d951-bdab-37cc-a03d-6fd3a969ec6f | -8.8818 | -45.88811 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8ce08a3-cca7-351d-a481-3544862137ca | -12.44837 | -49.59094 | 2026-09-18 04:57:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f81b2abb-2bcb-347a-bb76-489c057b75dc | -11.98757 | -52.46444 | 2026-09-18 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c351a2d6-7431-3c06-ad9e-287d54b38a02 | -9.74963 | -46.57511 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f23910-fbaf-3b08-94f8-8cd0b892bc31 | -8.50711 | -48.49606 | 2026-09-18 04:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6542772c-09b3-35a3-9c3e-35ec9f8457a1 | -10.29603 | -45.31663 | 2026-09-18 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc2b9ec0-c705-30bb-bebf-15a7086a9cbe | -5.83378 | -52.03121 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 576d2718-6ff9-34f2-a9c4-82e808f7cf20 | -9.3963 | -46.86729 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3da1b513-6017-3724-acc0-0686a54f9577 | -11.29309 | -43.39513 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de3b86c9-7771-3e97-8714-32ed966ce99c | -13.36127 | -46.30338 | 2026-09-18 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e8b25e9-419a-3d0d-9efb-a8fa1038168c | -9.76562 | -46.60327 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c922e6f1-aadb-367c-b39b-e7e39c3ceda9 | -10.67809 | -50.26176 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49017084-d516-3135-85a0-1fde94a503fa | -9.95491 | -45.68696 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6217fdb-1da4-364b-b593-b5b6a0a8f837 | -5.82911 | -52.08171 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e276795a-2949-33ed-aadc-f7a07c1db8f2 | -7.09063 | -44.07114 | 2026-09-18 04:57:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 888c7747-de51-3744-afa6-3f9f85a30f86 | -7.9332 | -44.82206 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f966186a-7ed6-3674-863b-699df401ffe6 | -10.66725 | -50.28679 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a3e632b-f9be-3396-8b4e-3e3b28b7f5f1 | -9.19119 | -46.74684 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6a9792f-e299-3012-8760-ebf9f3431a69 | -9.94272 | -45.31954 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b939a7b2-d7c3-335e-9a59-f52a77fd6a9f | -9.19374 | -46.75783 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d9575d3-b0a0-33cf-96b8-990690555503 | -10.66611 | -50.27135 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f25a9120-e4b8-3686-aa53-15b8d8a911ce | -7.66993 | -46.09029 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 910bea87-3722-388a-abb2-6d6ef1bbe87b | -7.18618 | -44.43853 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f044cc8-f3bf-3c57-a259-f53820b1fd18 | -6.27079 | -51.75007 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d35e62d0-9b9d-36df-beea-3b0548c0304b | -4.77365 | -55.70775 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ee9bf30b-6bc9-3ec6-9b37-8ed20f683702 | -12.39255 | -50.6973 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 762ec58d-5d12-3622-a3fc-55253e48ea7f | -9.78327 | -46.47726 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 233caf41-1647-387a-b85a-102e87f2072e | -9.94045 | -45.28506 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bfd8817-36cf-3176-97f6-66e5461c9d08 | -8.77854 | -46.90997 | 2026-09-18 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb0630fe-3454-3057-a55f-1098f80a101e | -8.46397 | -44.52532 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dfc7c0f-c7fe-3e62-9a6b-1d630cdb3e4b | -11.52338 | -46.86022 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc880bad-ea63-3e32-bfb1-a100161c1cf5 | -8.48853 | -46.8812 | 2026-09-18 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95adf4bd-905b-3466-a8d6-1af0f95e32e4 | -9.95432 | -45.69111 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be7530b0-316a-36c8-ab75-3325946b6b6e | -12.71952 | -48.26641 | 2026-09-18 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12d17abf-8ef3-353c-81cb-0811c44955b1 | -8.3597 | -47.54119 | 2026-09-18 04:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4af321e7-1f4f-343a-a2b8-805a1dd8a29d | -10.99164 | -49.73866 | 2026-09-18 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b310c30d-b997-3cc3-ae9c-8cd32f03f1dc | -7.04017 | -42.08313 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7777292b-3d99-3e9d-97b0-fd3a8a87463e | -10.54991 | -44.84881 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e0ae991-5d10-3c54-82d4-cb9aaba812ab | -10.65241 | -50.24628 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b7d8f042-bbe2-34d5-820e-740df1652c6a | -5.87386 | -53.56305 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44708b86-1640-3021-b14b-a7ae7958825a | -9.68801 | -54.34174 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c2ab528-949c-302d-901e-f15bb1f3f425 | -7.93629 | -44.83236 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e415d94f-8699-3a6e-ba6b-70c1cef54f36 | -8.65163 | -43.86872 | 2026-09-18 04:57:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df1eaaf2-50b3-3e59-8240-6bd9d0a41905 | -11.87893 | -47.57834 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db920278-b518-3aa7-aa6d-42c97fbd91e1 | -7.00185 | -42.16228 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7aa7326d-5aed-34ef-bdb3-09e7a841c789 | -7.80006 | -44.9046 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57de531e-187d-3eb3-ae43-0905d40a2822 | -9.19325 | -46.76133 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c24376dc-128d-33c7-b4f0-56eb29dde781 | -5.88354 | -52.0867 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44db5b0b-340e-3bca-8a94-6cd47015ad1e | -9.39537 | -46.84594 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cb25a8b-f0e2-319b-9c66-d265eac56579 | -9.85641 | -48.37928 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d1406c3-9569-3d32-97a8-c579b7840c13 | -9.46092 | -45.44765 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ad65ff6-5d15-352d-83de-fa52c98c97e9 | -8.71383 | -44.8754 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf804da0-c9ac-3e61-835e-0feb2b0bc9a3 | -9.79336 | -46.09648 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b09d622-e46a-3cd1-96cc-4ba62bf9afa8 | -12.43758 | -50.67753 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 999a3b6f-fe75-3dfe-8b38-1a39fcad892d | -7.67025 | -46.10854 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc974d43-767f-31d2-aca6-2b345fb38363 | -9.15321 | -49.9967 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37a7e687-a187-3b2d-8504-fdf94d1bf8d9 | -11.27395 | -54.11523 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0224945-7fa4-39e2-93a7-d9728184dab8 | -10.36949 | -50.45638 | 2026-09-18 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c8307de-2244-3ee5-b4a5-916e2335e84c | -8.88554 | -45.89232 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e32b2d4a-d648-3918-bbe0-1f61d2b3f653 | -13.23686 | -42.33763 | 2026-09-18 04:57:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| adfb903a-e939-358d-9b4b-01b23c3bac2a | -12.29428 | -50.74683 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de804687-e066-3e4d-96af-16df7f75225f | -12.16967 | -46.97874 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ededa27d-c9a7-3891-9c45-46873d9e833d | -6.77953 | -47.86361 | 2026-09-18 04:57:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eea66411-545b-3a50-8bdd-4ebbefbfe427 | -9.91711 | -46.52697 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53cd963d-d73f-339f-99d1-d23ca43c23f6 | -4.80579 | -56.08364 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d4fa4ce-a0e4-3715-84ac-a02c1e1180cc | -10.11905 | -45.56517 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README62.md)
