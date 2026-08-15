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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f78f5e1c-b04c-3e04-a390-16da37621644 | -18.58746 | -41.28041 | 2026-08-15 03:55:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1143e9e0-e3c5-3013-bb0d-5743997c7d0c | -14.44243 | -51.89865 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7362729a-fc88-3bd8-bd25-809e3ae7f3a5 | -15.12891 | -42.12905 | 2026-08-15 03:55:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5af1f2b4-6752-391b-bb03-ac2cc17e36e8 | -17.50874 | -42.37599 | 2026-08-15 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49f69569-78be-3cce-94e6-37af413a7813 | -14.42999 | -51.91967 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 69489e3d-b987-3128-8e6c-4b3a0436901b | -12.72373 | -48.42821 | 2026-08-15 03:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20cd2fe5-fc6e-341a-9f26-d40756469351 | -14.39824 | -48.95707 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17370dca-f618-3f2d-a314-46fc7d4f5b45 | -14.44635 | -45.68974 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed90436e-dd0c-3da1-9510-b2995f60193e | -10.42005 | -47.98154 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bb251ba5-9635-38c4-afc2-50177bf59ba8 | -18.4544 | -43.43605 | 2026-08-15 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7b00c979-2703-39a0-b02e-c1ce2079e87f | -10.72001 | -50.56385 | 2026-08-15 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 90cafc15-25e1-336b-8512-e98a065f459c | -14.43546 | -51.9291 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1df6abaf-fb71-377d-81f7-76dd235f7d47 | -14.45807 | -45.67592 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4344a6c0-9ab3-3c56-ba3f-c8098ff3ca65 | -14.43722 | -51.92142 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dc1afee0-aac6-3b51-a294-d71380442933 | -10.40661 | -47.9841 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5819c94d-d676-3e21-9ef2-f8b156ab0696 | -14.44618 | -51.91556 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 36eac309-cea7-317d-9606-5d8ce36e6f77 | -14.92255 | -46.62284 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c6cf5639-f32c-33c3-8629-b921831e1a67 | -18.45037 | -43.43524 | 2026-08-15 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b003748f-130f-37a1-b5df-fde46d337c86 | -14.40433 | -48.95872 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd4b7e27-3e71-378b-881a-85118970bd9a | -10.40765 | -47.97879 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d653ec94-2d09-3416-87f9-0ad4e75f87ba | -13.5379 | -46.25262 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d23cb304-c7b7-3aa5-8e19-1249fbcef028 | -13.68671 | -46.27005 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca964581-5936-3da8-b241-4dca39891e39 | -11.40948 | -46.3427 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67f29df6-e887-354e-95c7-c9e8fa01e36d | -10.6139 | -46.57177 | 2026-08-15 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68c8d747-0995-3a84-a3fc-999d75cce96e | -14.44425 | -45.693 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d2963b8-25b3-349f-bf9f-45e3a225918a | -15.10763 | -48.69336 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4031a98b-6ccd-3231-8ac9-dd12450e2760 | -11.41023 | -46.33421 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d844bee-4dd1-3b51-9d35-833304893fc1 | -12.13762 | -47.16259 | 2026-08-15 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a25945c5-3762-31a8-a486-c19e2203f03e | -14.7482 | -48.25219 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 740e83ab-2fd8-395e-9bc3-70af2196f2f5 | -14.40326 | -48.95475 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7a66ab8-97c5-39ec-861f-c27fd2c73562 | -11.67955 | -46.75548 | 2026-08-15 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c73aa37-2465-3388-8dab-b4c184689913 | -14.94886 | -46.62866 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 981db2df-f91f-3a73-b2ab-757f714b8808 | -14.44791 | -51.90798 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7e79b455-5a49-3283-85bb-60d8e97c9c92 | -14.4669 | -45.68391 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf318e22-b98b-36fb-873b-ee2f60dda8f1 | -17.90111 | -44.44497 | 2026-08-15 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4f74fa40-6059-3df1-ad58-8cf3a6c2443b | -11.48827 | -44.56796 | 2026-08-15 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98977401-b4ee-3848-9169-2450fd897666 | -14.45166 | -51.92495 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dff4afd2-fcf1-34cc-9922-73df6e2d02b0 | -14.92796 | -46.62329 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec25c75f-4f8b-3bf7-aaa3-da7e6355b4ce | -15.12496 | -42.12838 | 2026-08-15 03:55:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1200dd0d-2543-3f5c-8136-91eca5fb0da0 | -15.10614 | -48.69398 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05e11d59-a726-36de-8545-c82f7292fc99 | -14.91811 | -46.64464 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f5d08c-c611-3b51-8e6a-a736a1ea302e | -14.39926 | -48.95223 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88724bdf-7e0d-3d29-808a-9b4a70f42f9d | -16.10936 | -49.86732 | 2026-08-15 03:55:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4ea11bf8-211e-35ca-9681-e048c7e2ad8c | -15.15593 | -50.06889 | 2026-08-15 03:55:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d54c543-b4ec-3229-99f0-b8574d236376 | -14.92857 | -46.62025 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a5bfc9a-00f3-3615-b394-d4f39458d278 | -13.6855 | -46.26657 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dfd354b-3e50-3915-aee8-cf2e3d445b24 | -14.45446 | -45.67452 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 530d7376-d0d1-3614-8b47-8b6363e2933d | -11.71999 | -47.00707 | 2026-08-15 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc743852-770a-3e06-bc4a-8730b184f440 | -12.09786 | -43.1617 | 2026-08-15 03:55:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f3d6716-bbf1-3b4f-86a8-ef32658a66e5 | -13.4808 | -44.03836 | 2026-08-15 03:55:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48394a12-233e-3092-8ca5-120c9b1f7b5e | -14.40533 | -48.95395 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 140d602b-a712-3a17-b272-020425a5dd2e | -13.69077 | -46.26767 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f90e451-9a42-3e96-a9e8-bf4709fefe07 | -14.4402 | -45.69463 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eae9a52-07e2-3742-b2a3-eef1f39ac83a | -14.60766 | -46.74114 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecacf85f-68d0-3947-8cb5-f659794b5b66 | -14.45924 | -45.66999 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4d8fb8a-e8ec-3b62-bc26-e7fede36e780 | -10.60826 | -46.5704 | 2026-08-15 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 989fc286-8ede-3a71-968b-bfaaa5caf7d2 | -10.41285 | -47.98527 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 622ab2c3-a88e-3861-81da-d057d970c9d6 | -10.41828 | -47.97802 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2bebd17d-5a33-3533-969e-96edccd13bda | -13.65709 | -46.25312 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cceb644-d911-3b69-b456-a065ceb4f071 | -14.25943 | -42.18039 | 2026-08-15 03:55:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 060eb5d6-d42a-3e49-9169-2d59f858c100 | -12.03179 | -47.81401 | 2026-08-15 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5b969b1-6782-3ac8-8773-ad9b653f0a4f | -18.58465 | -41.27529 | 2026-08-15 03:55:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| c0f96a33-6355-3f26-87c5-4cf5667f2003 | -15.12404 | -48.69806 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a118394-97ba-3f7c-9053-0c3dafc4deb1 | -12.14336 | -47.16375 | 2026-08-15 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 390c1987-e36a-3d1d-8a52-b11031923d3b | -15.06703 | -48.67199 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d6e7772-35a4-34aa-a722-a19e8e263726 | -14.42276 | -51.91794 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 97e8d00c-acc4-324c-9a34-a8bbd00ca976 | -14.44578 | -45.6927 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d6ed187-7c88-3fc4-84dd-e6aec709b782 | -15.54342 | -42.30389 | 2026-08-15 03:55:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0ed74e6-d44f-37d8-b363-47de958a3bc9 | -15.61344 | -41.55381 | 2026-08-15 03:55:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c51be4d8-53f8-3e82-9218-5bff90668438 | -14.4407 | -51.90619 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 593cdb96-e078-3363-9080-da64a44edb8e | -14.91456 | -46.63504 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ed35712-294d-3779-b71e-47d673d981a6 | -13.4753 | -44.04231 | 2026-08-15 03:55:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd811ce1-b0f3-3995-8890-ae3beb222cb9 | -18.45416 | -43.43636 | 2026-08-15 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d8f514ac-21e5-39df-8e23-baa8ed7f4d8f | -11.40452 | -46.33864 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94767808-ef86-3c22-8b04-c02f84a11d2b | -14.57318 | -46.77368 | 2026-08-15 03:55:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb87ed8d-e2a6-38dd-8668-e588a84becf3 | -11.40861 | -46.34243 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 491b0226-8a17-3398-94b8-b5c833a71760 | -11.41024 | -46.33864 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d79ae65-89f3-30fe-90ee-54743d65ccb6 | -12.09702 | -43.16641 | 2026-08-15 03:55:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5706d2b5-6ff8-3731-9159-d09cdaf70445 | -14.69331 | -42.91534 | 2026-08-15 03:55:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7699b638-674f-3748-a0be-2f91e96136e5 | -14.42939 | -51.85408 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfba5f6d-cf0b-39a2-bed9-221b5d340116 | -12.19196 | -40.40511 | 2026-08-15 03:55:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0604993-a9ce-3272-8610-2a55b4215836 | -10.49166 | -50.15868 | 2026-08-15 03:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0354bd1-4d6e-3b5b-a5a6-38056661fdb8 | -17.89681 | -44.44389 | 2026-08-15 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65d238fd-c704-3b51-a9e3-1fbfc719f5e1 | -11.39978 | -46.32904 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc87942a-37ef-3f13-82eb-7798b8d5fa94 | -12.08049 | -43.18197 | 2026-08-15 03:55:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e24f8a77-842c-3f33-8ef6-ad1901900dff | -10.41385 | -47.98014 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 252d7934-98a1-3dd7-9d23-8638a3c9520c | -15.6511 | -48.2055 | 2026-08-15 03:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 631aa815-e2b8-36b6-9695-0f8cef63023e | -14.39419 | -48.94572 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87383986-412b-3e2e-8535-b4537ad27ef2 | -13.69599 | -46.26904 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a5754f3-301b-3b19-b074-6d0aa294c64a | -14.45947 | -45.67557 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 727a9952-0f6f-3db7-97a7-7ab8dde59fd1 | -15.10514 | -48.69876 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 176498ce-051c-307f-a4b1-5a61873c4700 | -14.43026 | -51.91836 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a6ec0c4b-7bc1-3aa3-a0d5-2976a41e5ccd | -15.65046 | -48.21035 | 2026-08-15 03:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41807dc9-dadf-38b1-85df-fa1ce48012c4 | -14.75016 | -48.24272 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f70cddb9-e165-384c-a8f0-27d8eae79b3f | -14.22671 | -45.41212 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2936905f-8d42-3791-83c4-5127162533e1 | -14.75445 | -48.25156 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fc9e4f2-433f-35f6-a7ee-351b8fe26515 | -14.43174 | -51.91203 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 91c2136a-1d9d-33cf-ab5e-b8af0a825e9a | -14.91604 | -46.62778 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29b902c9-2551-3d8b-a98d-839530a919f8 | -14.43963 | -45.69762 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82546d68-a017-341f-bf86-f4fb9f60406d | -14.45042 | -45.68816 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
