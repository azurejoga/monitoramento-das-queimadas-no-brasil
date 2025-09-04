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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ad4f5e9-1bfc-35dc-911d-4795e025ae92 | -15.02781 | -48.11053 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14d5305b-29e0-3da0-a7ff-f61a44ff6e42 | -12.18744 | -53.8952 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54285964-cad4-337a-8ed8-0e57d38d4115 | -9.04377 | -47.00903 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67d446d2-bb95-329f-ab0f-e399506ea4fb | -13.30627 | -51.76852 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08744e77-334c-3827-a29d-936159fa8c35 | -15.03111 | -48.11107 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61bef91c-56f9-3d15-94b6-31795c3ac963 | -10.47831 | -53.63868 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4545e21c-7187-309b-8bad-a7d9019e288d | -12.49639 | -48.07219 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0e59548-0252-39d2-845a-af3ab60876db | -12.89731 | -48.03292 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a12d4166-9f11-3dd4-bec7-8118a8c65989 | -10.72248 | -47.95195 | 2025-09-04 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e6a10f8-76ad-3d14-b627-854bf8bf19df | -14.75584 | -48.08771 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5ff1a34-150b-35e2-a896-9f7585f4b069 | -11.65141 | -54.52012 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 133e5b11-5af7-356b-aa50-4809204bf1a9 | -6.75386 | -58.72846 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8afb263b-b039-3892-a0e2-2a54bd28758e | -11.62362 | -52.19409 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bb66c45-7d72-31da-b1e3-b956acee8463 | -8.89705 | -45.82726 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4dd39252-de64-3aef-840a-bb46e5a94bc5 | -14.56623 | -48.03825 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7013bbcc-efee-3750-a4cb-980f7b8da3a0 | -12.17888 | -53.89354 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49ee1e6f-8c69-367a-8f5b-61aec82f0f91 | -10.46587 | -53.6249 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf697502-691d-3246-a388-ce54f2ddb912 | -11.64775 | -52.19336 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3729503-39d6-3215-bcb1-8db958a6aaa0 | -10.21461 | -51.12978 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17e83b60-d872-3265-bc85-9cb91d8fe4ee | -12.18112 | -53.8813 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc23b33-534b-310c-a20a-9c907b9f672c | -14.38799 | -53.0703 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c036bda-573e-3b07-becc-e2f2ad97744b | -11.05828 | -45.40427 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96416cd8-f79d-30cb-9591-08e5cdb2122d | -8.47117 | -45.05723 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b5f57e87-15c8-308c-8c24-bd1aff901df1 | -9.30346 | -47.08986 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dabe5b90-7e98-371f-8bb7-149d65c45c7d | -11.6534 | -54.53471 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 889d1a03-b884-36b7-aaef-a790b34464d4 | -13.86625 | -47.97089 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| af8fbbe6-1e2d-3d7e-98b3-66406c30b982 | -11.86017 | -51.43583 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3fceb44-d542-373a-8bce-aa6fc1c64247 | -12.48593 | -48.07409 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 169f88bc-7c9d-3f50-9887-1318e0f2a636 | -8.03373 | -45.37948 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 107cc06c-9cb9-3cbb-af14-8cddd292e037 | -14.78865 | -48.16214 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 901762b9-383b-30ab-9313-929030cb60d0 | -8.89426 | -45.82316 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4883dffe-058c-3e40-b95c-b27f1d0cfdad | -9.6048 | -47.03122 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1b2e6054-9280-305d-a3aa-4cc7c75b35c0 | -13.50008 | -47.01501 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe7b336f-018c-32eb-9358-e10acc200709 | -6.74753 | -58.73137 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2c04fefc-28b3-3500-ae86-e177172779c7 | -10.98553 | -50.92303 | 2025-09-04 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae590da1-217f-36cf-a11d-948f0a2365a4 | -10.50732 | -50.43826 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30720f65-bed8-3532-8acb-bf9322adc18a | -11.58081 | -52.15783 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfdd4c1d-a0a2-3b61-b2c3-f1c6ba6c7d82 | -7.68458 | -50.27016 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b00b458-6527-3749-8825-601207eed433 | -7.69803 | -50.2539 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b6c8203-cbec-3d92-aaad-3cd9cd4c4a2f | -11.238 | -44.96313 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c30a129c-23cc-3d41-bd1c-9cfc2c5200cd | -8.91048 | -45.11935 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a1b21e0-ba11-3b33-bca2-8626f21caa34 | -8.47685 | -45.06573 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c4685ee-af7f-3446-bb1f-92ad9c9bf10f | -12.91209 | -56.93855 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20713611-73f6-38fe-ba3b-4094a2b139c9 | -9.61579 | -47.02583 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bbf56a9-c663-3685-b3aa-d3ad3c5ea997 | -13.30843 | -51.76531 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f1ff095-b4b8-3de3-b1dc-c04fa785de48 | -10.48871 | -46.77108 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5fc188a-8614-335a-b4e5-7b32ca4aa02e | -9.45471 | -46.79667 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5345c6f-19c3-37e9-b5d2-26216bc9caf4 | -9.72519 | -48.3189 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 457e70f4-dada-3277-a29d-604f457f25b4 | -14.54255 | -48.05979 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab89d60c-719f-31a9-9ceb-ad059d24b362 | -13.74512 | -46.94622 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b743f6f5-4e73-3885-af56-c571d70665c8 | -14.77819 | -48.14221 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 414890ac-97ac-389a-b03a-b92a73882e4f | -14.55852 | -48.04425 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52196439-e734-3892-be9e-933b054c66b5 | -6.76213 | -59.67494 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f99b9a5d-08ea-37e2-80ab-77ce363a35f2 | -9.06738 | -46.98785 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 534d57e3-723e-3b3a-bd4d-ea028edb451e | -12.56857 | -43.78549 | 2025-09-04 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd7ee693-a485-3df5-997a-393d1b17e9b2 | -14.90602 | -49.62895 | 2025-09-04 04:27:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f82fd235-7c5c-3a3d-a642-2da026290b25 | -9.83267 | -46.63848 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d889461-663e-3e9d-be7a-7bf039664580 | -14.20816 | -48.08857 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d40b64e-8bfa-37da-a8c2-2d2a6ff44eeb | -10.96739 | -49.74618 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2be86e73-95a8-3593-b0aa-5c7e2f80a35c | -10.12638 | -46.29887 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e9537c6-2ae8-3a90-a592-eae3d0aed61a | -13.39751 | -47.06459 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6009e8a-628c-3928-b289-efe870c2716d | -12.57103 | -48.26845 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03c2debc-381a-3afd-b1f8-6ddf94d9ffc9 | -8.89079 | -45.77879 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5e2348c-578e-3547-9abc-1b13cc371daa | -7.2709 | -57.55979 | 2025-09-04 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b02a22a-4e82-3aa8-8214-dd7dce6833cb | -9.99548 | -46.88296 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43e722f4-b5cf-30e9-9924-8f42daab976a | -9.06684 | -46.99133 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7feaf086-7e78-3bfa-972e-62e4862d1a5b | -13.50807 | -50.80908 | 2025-09-04 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e32470b9-902c-387f-a172-2c351f341edc | -9.27092 | -48.55577 | 2025-09-04 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 578da602-7ecc-350d-baef-9b827628dc11 | -7.75981 | -49.55443 | 2025-09-04 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1e26e59-085f-3fdb-b789-044d30f28569 | -13.45506 | -46.83776 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dd70a60-ac77-3b5c-b2b4-1626e95f12c2 | -8.76117 | -46.11433 | 2025-09-04 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9da14ce7-7dd7-3afc-a0e8-4978eb0ecb9e | -11.73746 | -47.75062 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3d3f0f59-7f0b-3f74-a7da-432500c2df9f | -7.97541 | -46.35607 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d56131c-34a6-3616-8db5-e45454f84246 | -12.99406 | -48.06721 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0e103af-bf2a-3c8a-aa71-5d356df15d57 | -12.50025 | -48.06919 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0839e7a3-4ca0-30ea-b058-c135e0e80bd8 | -14.82109 | -48.23665 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbabccfa-a3f1-3281-9ed6-32567619dfa7 | -14.82099 | -48.34574 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40c4da7f-dc00-3835-af17-1bc97395c86a | -10.70219 | -49.02016 | 2025-09-04 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9c0dd82-ee4c-3c21-8f8d-a7cb1f72ffcc | -7.68427 | -50.2686 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b211219-7f05-3f83-b4c5-80009a0729ee | -10.5319 | -46.7567 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d46e555-cb10-39b7-9e88-b067def2a7ef | -12.89941 | -56.94226 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5785a510-1adc-3dfe-80b9-34d42fa78002 | -15.05598 | -50.04527 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cf21389-5dd8-3e23-a7ec-4c3610d99a5d | -9.99879 | -46.88348 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e203d1a-fde6-3f1e-87e6-dc736e5ac740 | -10.97304 | -49.75504 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88101ddb-ec2f-31ac-8c2e-744d019ea36a | -12.90974 | -57.00146 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f2eec27-6d2d-3219-93c1-3faf59cad831 | -8.87032 | -47.93686 | 2025-09-04 04:27:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1872544d-bf69-3f31-9262-bd2ceefce39e | -11.64302 | -52.19761 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a29d7807-0ed1-3b49-8131-0b9bed9bc621 | -8.91388 | -45.11992 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 270f405f-808d-36e0-97db-fbf359c31401 | -8.0018 | -50.07328 | 2025-09-04 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a50fb9f6-231e-3257-aa3f-82d15fd43bd7 | -8.36474 | -48.33165 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1f56219-03a4-38e6-938f-643060cbb5f6 | -11.04732 | -45.14763 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 23eba573-5f24-3430-b0cc-28ebc189f205 | -15.00798 | -50.03326 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e959d8a4-8ee1-3d15-b6ef-4ddb10c0cb1b | -11.95974 | -45.77101 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91cd55e2-db61-3b8f-a580-0fb143113fb4 | -8.86628 | -52.02514 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef824657-918e-327a-9978-4fc1e21064dc | -13.48784 | -51.81237 | 2025-09-04 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dae4cba-7a57-346b-acc0-5ec5a2e7e426 | -12.52574 | -53.80771 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aabe3f1-48be-360d-b630-915f86b384fb | -10.47022 | -53.62562 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2e27b76-c34e-372b-9a02-ef2d8e1af912 | -8.85887 | -52.02024 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11c0ed32-586c-3e74-8acc-f61c4de35f86 | -13.0023 | -48.0794 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d0862b7-07c8-37ee-818d-9ba0158ec48e | -15.04296 | -50.08212 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README42.md)
