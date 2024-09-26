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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a19cac3-e220-39f9-9039-895619847f7b | -13.99652 | -56.3705 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef466218-e595-3639-bfcb-5b743fd4f8af | -13.98353 | -56.17218 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9339089-1041-3e6e-8737-afe9296c11bb | -13.98023 | -56.17163 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 046b7f44-1578-3f65-95cd-9e197c41388b | -13.97748 | -56.16754 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76ad34cb-d47d-3c12-ae5b-8e002e76c215 | -13.97474 | -56.16345 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d45baf12-a260-3f90-b66b-052a1e0d22e5 | -13.972 | -56.15937 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1964e81-b299-36d0-8d0a-af8a7a3aa8f2 | -13.96869 | -56.15882 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb7c00b4-02d2-3969-91f2-8ed5c0c6606e | -13.96539 | -56.15828 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84b7f0a7-cce4-3ba7-ac8c-60817b3d9afa | -13.96483 | -56.16182 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ea57ff-6aab-3044-a92d-f3634595e649 | -13.96209 | -56.15773 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3309b65d-a25a-3b3d-ab7a-88e7723b05cc | -13.96047 | -56.14656 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecfb4d96-5d37-346a-926f-8198cde1fb1c | -13.95991 | -56.1501 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce503685-d18d-3493-9aca-de7ac0c8c51e | -13.95935 | -56.15365 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51a58f6e-4d63-3db2-bb97-da7927ef6eba | -13.95772 | -56.14248 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17017c19-b7c8-31dc-90e7-4ddad2c91b35 | -13.95716 | -56.14602 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95bac195-23ba-3fa6-af31-1268e38edc29 | -13.95442 | -56.14193 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3a39c26-697b-3bfd-a3c4-abec891eaefc | -13.95386 | -56.14547 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31dce39f-1542-3be7-806d-9461fe1413e0 | -13.83209 | -56.3762 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e894234-b945-30c8-905e-272d38b0b2ca | -13.83152 | -56.37975 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18d4a733-e05d-382d-8b32-b00cdfb2d2ed | -13.82878 | -56.37565 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17c01ee8-050b-3299-ae51-86d9ce5b8305 | -13.82821 | -56.3792 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bec5bcf7-730a-3e7c-8ee5-7b52f21b2b46 | -13.78856 | -56.50023 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d86c5a3a-96cf-3c00-8f15-112bc182493d | -13.78799 | -56.50378 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84bf66ce-f2ba-3e7a-958d-16e4a165450c | -13.78524 | -56.49967 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52ef1129-6e56-336d-a9ce-0e0848d455d9 | -13.78468 | -56.50322 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0182f9e4-5042-3e67-be86-5c798ed70a30 | -15.60569 | -56.95231 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 50728bf0-a6d4-3d8f-8e71-43be0d44ddab | -15.60511 | -56.9559 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be2ae8ea-5027-36f7-b16f-cb9979cd1950 | -15.60351 | -56.94464 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 107dcfe7-d520-3466-9a70-a363ba91966d | -15.6018 | -56.9553 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 29db9b0d-f95e-3461-80fd-825aa1c5cb2e | -15.5946 | -56.95782 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39da1b89-9f42-3eb2-a49d-4d3044ce9aaf | -15.59186 | -56.95363 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb1f0139-afaf-34f8-affa-a134dfafc8df | -15.59128 | -56.95726 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5f1b991-839e-37c8-bcce-4fa0cb38f5ac | -15.58866 | -56.93109 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a3da58eb-1996-30e7-803d-8db6505e02e0 | -15.58809 | -56.93463 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 006979b3-ac04-3731-8cae-747f864b748a | -15.58797 | -56.95671 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd01c2c2-d1fe-35c1-a98f-1ad0964fa6f0 | -15.57873 | -56.92932 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 920e65d0-bfec-3a58-a17a-1cc69f579816 | -15.55887 | -56.92589 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8b40804-4794-39aa-a3e2-6155ed607d8a | -15.55772 | -56.93308 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d68945b-4b50-3cd1-93b3-7fb54c68e76c | -15.55441 | -56.9325 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e69a3eea-9c08-313b-b918-6d1f7b163a1c | -15.55168 | -56.92833 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e0b704e-4874-367d-89de-a3fc3a5e0148 | -15.5511 | -56.93192 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67f907f8-6ccb-3350-a783-3d1f3026befe | -15.54779 | -56.93133 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 727146ab-e9e7-3587-ace2-00ba75e12d1b | -15.54621 | -56.91999 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf3b5592-fe75-39c0-9867-35998315bbce | -15.54563 | -56.92358 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 69e10ac9-510b-340c-abb3-436b58e002b0 | -15.5429 | -56.91943 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d08bb908-069e-3f44-983b-7ad29dc924ed | -15.54232 | -56.92302 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f141108a-db88-3d98-8ac0-0a2976566874 | -15.60625 | -56.94877 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d357e046-1e74-3758-8f6c-f56454d95c46 | -15.60407 | -56.94111 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 844402fa-65c1-370d-b392-4ce0fb315ef8 | -15.60295 | -56.94817 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ab9045c-d9b8-3306-a74c-9cb2f9853ee7 | -15.60122 | -56.95895 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| defdaf61-3e9e-3b96-9d0d-b41585dff671 | -15.59518 | -56.95418 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31449d5f-7c3b-3ff2-866e-f0b3daaaafe9 | -15.59402 | -56.96146 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bee7686-0166-3ff7-92ff-850971ce1801 | -15.59197 | -56.93168 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e11512b3-643a-3fb0-bac4-90d94fcbdacf | -15.58535 | -56.9305 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b575a72c-ea73-3bce-b31c-195155ba0df7 | -15.58479 | -56.93403 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8550adb2-0e93-3291-be38-f5b1750d91ba | -15.58204 | -56.9299 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 428210f8-9286-37c3-b959-eea61b12535e | -15.5793 | -56.92579 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ca234af1-a8b2-3386-8db5-d4e25b4f6187 | -15.57599 | -56.92521 | 2024-09-26 04:59:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 646da653-393b-3451-802b-dfa782b5523a | -9.40578 | -56.8698 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf54b188-dac6-3050-9974-392bdb265208 | -9.40357 | -56.86171 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cac97634-7ffd-3396-a414-828ae5d670a8 | -9.40296 | -56.86547 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d2df37a1-7784-3609-ba57-a19bb1bb423c | -9.40236 | -56.86924 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 081e530b-d6f2-35f9-83a9-59bfcdd7c70f | -9.40135 | -56.85369 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a71e32-eaf9-3be6-85dc-1ddef0c63ced | -9.40075 | -56.85743 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3044f2c5-5f9a-3de2-8a90-41f5a1d5ac3b | -9.40015 | -56.86116 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dea780fe-2eb6-39e8-8b5c-95cffc018e9d | -9.39954 | -56.86493 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc9b8e10-93f8-39ef-a1ae-99a49ad485ef | -9.39893 | -56.86871 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b6c99288-0aee-3add-a781-9941f7b9764d | -9.39794 | -56.85312 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d43039d9-614c-3fd0-9754-de0bc5b53892 | -9.39733 | -56.85686 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed572b87-bed2-3323-9293-026d1b6267e7 | -9.39611 | -56.86439 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a11cd3b-252d-381a-bcc2-f444480547ef | -9.38987 | -56.85954 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7da2380d-01e4-30c5-a114-25eb6b3d7583 | -9.38926 | -56.86331 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a20abba-c0b5-3f8e-b72a-f1186fc6a624 | -9.28478 | -57.61573 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af840e6c-82bc-3175-8d7e-3cdd4da18632 | -9.28363 | -57.57838 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2319576-70e4-3955-b833-805eea690adf | -9.28298 | -57.58235 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28b4333e-79d5-343a-9968-d36be1fa88db | -9.2801 | -57.57779 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eef0f56-688d-370c-b133-92732fcfa987 | -9.27945 | -57.58175 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d325595f-6ceb-31c9-8932-baf2855359fc | -9.27593 | -57.58115 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2cc6060-64bf-363c-83d2-5b5e7310d984 | -9.27527 | -57.58518 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 336be2ab-b42e-3901-a08f-128df8b58807 | -9.90915 | -57.06003 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 21596d39-9028-329e-aa24-2203bd354c6f | -9.90634 | -57.05565 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 80698c65-1ec5-3828-9d16-7af5edb7b887 | -9.90573 | -57.05945 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a50d0991-0cef-3eb4-b146-ef41c5ccddd6 | -9.90291 | -57.05506 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 56289462-451e-3637-af9a-b5ee94a77c84 | -9.9023 | -57.05886 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1b59ff37-aaf1-3014-a9b2-2a7b96f95621 | -9.76561 | -57.78354 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b635364c-37fa-30b0-9258-16035330e4d1 | -9.76494 | -57.78759 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebbef2d0-1fb0-338d-8f96-afd593a87302 | -9.76427 | -57.79166 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b716d7a1-7b10-3f0e-819c-98732988262c | -9.76359 | -57.79574 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d565b3e-ab26-3777-b1e2-2fdc60af31cf | -9.76341 | -57.77484 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cdc3680-be56-342e-8823-88023d9156ff | -9.76274 | -57.77891 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 762a1ae0-bc98-390e-b7c5-709c5cda6f5b | -9.76207 | -57.78296 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17e1c432-f36d-3ce5-9a66-c0118d442a05 | -9.7614 | -57.78701 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f21caed7-fe3f-309d-bae4-4fdda3e198d0 | -9.76072 | -57.79108 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a0d1e2e-0713-377b-b4b3-4c9cc8378b46 | -9.75987 | -57.77425 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90c0cef1-c80f-3e74-8bda-421da0c8d7c3 | -9.75785 | -57.78644 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddc950f8-fd43-38cf-9b0b-7ad3e8aa88bd | -9.69954 | -57.19865 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f56f146-6bed-3494-9040-d1772cd624ea | -9.69891 | -57.20247 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd22ecc9-4295-3adb-95fc-442b7d00d8ec | -9.69828 | -57.2063 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88a4361c-1261-365d-966b-7aaf36d44121 | -9.69783 | -58.08094 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 067e7106-b2ba-32aa-afe1-0703beda9b6c | -9.69723 | -57.19818 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README131.md)
