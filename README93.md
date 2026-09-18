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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88c18f02-5d31-3be2-83b0-ef88844c05cd | -9.68003 | -48.31705 | 2026-09-18 12:27:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 3435271f-952c-3861-928e-dc6de3475117 | -10.66932 | -50.25074 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 900c67af-394a-342a-8ddb-bd4f6bd2d038 | -12.55535 | -50.70384 | 2026-09-18 12:27:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d678f316-6ed8-341f-ad56-6e3aa0a37ea5 | -10.67248 | -50.22382 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| bb7f0be6-801d-3590-9173-e47b95643427 | -9.84813 | -48.376 | 2026-09-18 12:27:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 6b4b17f6-2b45-341a-bede-10c27a80fc76 | -12.62344 | -50.90221 | 2026-09-18 12:27:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 508565b1-32b6-3cef-8052-a464e1140c87 | -9.7004 | -54.82226 | 2026-09-18 12:27:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2919fb15-c7fd-3c75-9f4f-c3a131f89316 | -13.42658 | -51.90701 | 2026-09-18 12:27:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 520b0f57-d3a3-395a-a156-ec216d10844d | -10.92485 | -56.41152 | 2026-09-18 12:27:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 87173bc8-6cc0-3972-b11f-b134007f4b4e | -13.431 | -51.90096 | 2026-09-18 12:27:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 4aeed941-ecf9-3595-8e74-d4fa2acde4b8 | -10.81177 | -50.19179 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| eb9f912b-847e-3fda-a9e5-6963fcb0fd5a | -10.67611 | -50.47191 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 34ab1e01-3b2f-3623-9ff9-7d25477e568f | -9.83291 | -48.41761 | 2026-09-18 12:27:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8fb4eddc-18d2-3ed1-8942-1924e7d68a97 | -10.65587 | -50.48878 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 09d1e0ed-1f57-3285-b3b8-37c4800c681c | -10.82738 | -50.19933 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| cb434039-5b3e-3f53-ba06-0dd42ddf4337 | -10.68392 | -50.25242 | 2026-09-18 12:27:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0b5a5fa8-6f9f-387a-9a19-8397b089bc27 | -9.83694 | -48.38115 | 2026-09-18 12:27:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 252.8 |
| ada20dae-d7e8-3dc0-8410-91eafb7d7971 | -18.881 | -49.51736 | 2026-09-18 12:29:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.0 |
| 1c71acc4-5017-3e7f-87e1-29e5a1b7866c | -18.8845 | -49.47672 | 2026-09-18 12:29:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| 2a8cc24b-b9b7-3496-9bd3-284647afc757 | -18.88662 | -49.48384 | 2026-09-18 12:29:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 0613dea1-350a-357f-97b4-80f1be665cf6 | -18.88338 | -49.52449 | 2026-09-18 12:29:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 59604089-84e3-31ec-8239-882b07bde727 | -20.04562 | -57.19456 | 2026-09-18 12:29:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7dab25db-3667-3ce3-9c5a-e926dc605e87 | -20.04418 | -57.2063 | 2026-09-18 12:29:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b79494e8-6761-3ebf-9a06-333372886752 | -10.8279 | -50.1815 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| c2ab4474-7e59-3743-9de9-84d5926b44de | -8.4675 | -44.4984 | 2026-09-18 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6ad8e47e-ea6d-3561-aa18-55cfd1faa8e7 | -11.0643 | -48.2678 | 2026-09-18 12:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| eecf52ab-cd42-3689-92a1-72e6ee65908a | -19.5539 | -47.6346 | 2026-09-18 12:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| b318f587-575b-318e-afde-dfc64dd806ff | -11.064 | -48.2898 | 2026-09-18 12:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 600a8b97-6c1d-3b57-b7a5-3ccb1676b2d4 | -13.6725 | -45.9668 | 2026-09-18 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 680a7f8c-62b6-35cb-9e89-de530de82276 | -10.6189 | -50.2466 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 42451eb9-0769-3838-a8ab-a7774674d5be | -8.4329 | -45.7337 | 2026-09-18 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 43dace31-e27e-3050-ae23-4404fc22d80e | -11.8115 | -46.8158 | 2026-09-18 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| e4a26097-918e-38a9-950c-6716f3698c3f | -8.4331 | -45.7111 | 2026-09-18 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| dc345b2f-f142-3552-a419-103bf7fba98a | -10.6758 | -50.2406 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c7b2b8ea-6df4-3a8e-85b4-807a99bb317e | -11.083 | -48.2875 | 2026-09-18 12:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 35df148e-62dc-3d6f-b7d6-ef945ca7dba2 | -14.1732 | -45.1875 | 2026-09-18 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d15514b9-8eac-39a7-b198-b97b34141b32 | -7.6574 | -46.1013 | 2026-09-18 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 2201f38f-ac18-3069-af1b-27257960705c | -10.4866 | -46.2909 | 2026-09-18 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a86b1916-1aba-318b-b294-17048fba6e36 | -10.3307 | -45.3112 | 2026-09-18 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3cee7f62-3e8b-3413-9ca6-a4e17ff05555 | -9.8505 | -48.3834 | 2026-09-18 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 67d94f34-9855-35e2-9183-78a913d8760b | -7.0352 | -44.6396 | 2026-09-18 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 83accece-e05e-3030-ac98-f9410c19aec0 | -10.809 | -50.1836 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9964f7ff-21b2-3f23-af59-da55a9c29394 | -8.8948 | -45.0253 | 2026-09-18 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| eb3790a5-9ad7-3015-b08a-7892c1c4ae50 | -7.6577 | -46.0788 | 2026-09-18 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c987ded6-224e-391a-9ce2-0c0f37d717e4 | -10.6944 | -50.26 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| f3872ed3-f118-37ec-a38b-eb38bb03af3d | -10.6726 | -50.4758 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c29ad983-1655-3f7d-8e1d-82ddb2c98498 | -4.5587 | -42.9523 | 2026-09-18 12:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2ab2d0f9-2d94-31a1-9981-c8c014b578f4 | -7.0164 | -44.6413 | 2026-09-18 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 220.2 |
| b244a8cf-b803-3822-b769-888ecc8d57d2 | -10.6755 | -50.262 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d1adbb29-e77f-399c-a483-1c7c09ae3c2b | -9.8316 | -48.3854 | 2026-09-18 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 93a90803-a129-33f0-bf89-352f129367f2 | -9.8502 | -48.4053 | 2026-09-18 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f01a2601-6e70-3f5f-9f34-de525e2b3403 | -11.2975 | -43.3851 | 2026-09-18 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| b9630d68-5426-3059-8fc7-dfd296d631af | -8.9138 | -45.0232 | 2026-09-18 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.5 |
| e7dfb5b4-387e-35c2-931a-a954b1df9c28 | -9.7308 | -46.1112 | 2026-09-18 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 76960444-790f-3816-8392-5437bb1205e2 | -10.8087 | -50.205 | 2026-09-18 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 113eb3dd-2f8e-34b7-acaf-5f522b2f02a4 | -7.5494 | -45.6839 | 2026-09-18 12:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 28aa368a-3e80-30f0-8570-c4a24b52153f | -12.5345 | -47.0738 | 2026-09-18 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3057c076-2b26-3f12-8929-5bd4c3edf83e | -13.6341 | -46.9304 | 2026-09-18 12:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 978aeae7-52b0-33b9-81aa-d49f7644e9b7 | -4.5774 | -42.9512 | 2026-09-18 12:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 527d0c5c-81c8-365f-98cc-75a7a78cb23a | -12.0676 | -47.4974 | 2026-09-18 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 1bf61801-147c-365d-a09d-62452f408296 | -11.3437 | -44.0141 | 2026-09-18 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 6f6c3773-8497-3925-abd9-f3f08e2ce69e | -12.5685 | -50.7523 | 2026-09-18 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 57824a9f-bc5f-31b3-94e0-3cc00bb85621 | -11.3442 | -43.9906 | 2026-09-18 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| a7bee6b5-88b0-3e10-b8ee-df198095e17c | -4.5772 | -42.9746 | 2026-09-18 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 07e0ce76-c0b6-3ab7-859b-68b14ae0e553 | -14.1732 | -45.1875 | 2026-09-18 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 1c61c906-0dbd-3a55-b22d-b841716c88e3 | -13.6341 | -46.9304 | 2026-09-18 12:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fd844d0f-c69e-3c7d-ad28-86a6ac8ce0b5 | -7.6765 | -46.0771 | 2026-09-18 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e80752fd-2b68-3f65-9fed-c9458cc9ceb4 | -10.3307 | -45.3112 | 2026-09-18 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| dd0b8606-5005-3ee4-8f5a-8b59ff9abb17 | -10.6536 | -50.4778 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 8bf19dde-4eda-34a8-ad06-ea2c574e181c | -8.452 | -45.7092 | 2026-09-18 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 90f426d3-faa7-309e-b83b-4587b00f89ad | -13.2485 | -46.9226 | 2026-09-18 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f6167074-6b97-3033-af2d-3551c5d3a52f | -7.6574 | -46.1013 | 2026-09-18 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 62789e11-0097-3d86-b389-5a36e706133c | -10.6944 | -50.26 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 39897e0b-b980-3578-b080-7c1a2642354f | -11.0636 | -48.3118 | 2026-09-18 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| f4219686-81e7-3311-b7b4-82584d13d03b | -14.1737 | -45.1641 | 2026-09-18 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 5d76432c-29a7-35d6-a099-00e161eb39db | -10.6758 | -50.2406 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 2864718b-d7be-3a3d-bd3e-84e3a509e4b6 | -10.8279 | -50.1815 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.7 |
| ef514587-41d1-3f76-9840-f671bd7ec621 | -12.5876 | -50.7499 | 2026-09-18 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1134bc95-879d-3270-842d-472ffbc00214 | -13.6531 | -45.97 | 2026-09-18 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e9f72ccc-a3be-3cfb-804f-dabda693c46d | -11.083 | -48.2875 | 2026-09-18 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 03fde472-a44b-3d9d-b4f3-8fa01f1af438 | -13.3052 | -51.3449 | 2026-09-18 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 304b26bc-0fe9-34d5-b5f9-49108f90c0fc | -11.064 | -48.2898 | 2026-09-18 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 098a7e6a-aaaf-310f-9c23-dab4c25dee79 | -19.5539 | -47.6346 | 2026-09-18 12:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 3c18891f-0e86-3c5e-8411-3efde92426da | -13.286 | -51.3473 | 2026-09-18 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 092c5f70-e888-35ac-b902-496df4bacd26 | -11.2783 | -43.388 | 2026-09-18 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 01d58036-5e86-3cc5-932c-6b8abe05c76f | -11.3442 | -43.9906 | 2026-09-18 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 6f968c62-139c-3346-abac-9bf12774c4be | -13.4303 | -51.9036 | 2026-09-18 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 249.8 |
| 1863df09-5041-3d39-8117-c116e91d64cb | -8.8948 | -45.0253 | 2026-09-18 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 42f05fec-5f68-300b-97e9-bfb4df788f8e | -4.5774 | -42.9512 | 2026-09-18 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 290.9 |
| 383544bb-fa2f-3367-85a6-96aac4f38dfb | -10.6726 | -50.4758 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| e4e8f8ef-9e31-3d46-86c7-cd0c5a650db2 | -11.2975 | -43.3851 | 2026-09-18 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 38a04c3a-30a5-3f9d-bd44-c95410f1e924 | -10.809 | -50.1836 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| f08bf49d-17be-3476-9808-fc74f2fae9a2 | -7.6762 | -46.0995 | 2026-09-18 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fc1a14e3-ad19-39ce-bb2d-cdc3ea94727f | -7.6577 | -46.0788 | 2026-09-18 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 190.7 |
| ac09b8fa-00a5-3de9-aa93-16b559c0252c | -13.4307 | -51.8823 | 2026-09-18 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 97635aa6-2541-32cb-b84e-b47b6510c190 | -10.8276 | -50.203 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 64d45783-0e03-3e26-adcb-556e2d7ed123 | -7.0352 | -44.6396 | 2026-09-18 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c92c7162-7c48-3a52-b2e6-655f769a4683 | -9.8505 | -48.3834 | 2026-09-18 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7a97818b-5fde-398f-bd53-1c67b2060876 | -11.8753 | -47.5679 | 2026-09-18 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7075f7bf-122e-3c41-b245-0e95c02f5529 | -8.9138 | -45.0232 | 2026-09-18 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |


[Clique aqui para ver as próximas entradas](README94.md)
